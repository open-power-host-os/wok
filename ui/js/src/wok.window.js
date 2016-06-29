/*
 * Project Wok
 *
 * Copyright IBM Corp, 2015-2016
 *
 * Code derived from Project Kimchi
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
wok.window = (function() {
    "use strict";
    var _windows = [];
    var _listeners = {};
    var open = function(settings, target) {
        settings = jQuery.type(settings) === 'object' ? settings : {
            url: settings
        };

        target = (typeof target === 'undefined') ? 'modalWindow' : target;

        var windowID = settings['id'] || 'window-' + _windows.length;

        if ($('#' + windowID).length) {
            $('#' + windowID).remove();
        }

        _windows.push(windowID);
        _listeners[windowID] = settings['close'];
        var windowNode = $('<div id="' + windowID + '" class="modal-dialog"></div>');

        $('#' + target).modal({
            backdrop: 'static',
            keyboard: false
        });

        $('#' + target).modal('show');

        $('#' + target).on('hidden.bs.modal', function() {
            $('#' + windowID).remove();
        });

        $(windowNode).appendTo('#' + target).on('click', '.modal-header > .close', function() {
            wok.window.close();
        });

        if (settings['url']) {
            $(windowNode).load(settings['url']).fadeIn(100);
            return;
        }

        settings['content'] && $(windowNode).html(settings['content']);
    };

    var close = function() {
        var windowID = _windows.pop();
        if (_listeners[windowID]) {
            _listeners[windowID]();
            _listeners[windowID] = null;
        }
        $('#' + windowID).parent().modal('toggle');
        $('#' + windowID).parent().on('hidden.bs.modal', function() {
            delete _listeners[windowID];
            $('#' + windowID).remove();
        })

    };

    return {
        open: open,
        close: close
    };
})();
