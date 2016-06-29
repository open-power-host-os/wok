#
# Project Wok
#
# Copyright IBM Corp, 2015-2016
#
# Code derived from Project Kimchi
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA

import gettext

_ = gettext.gettext


messages = {
    "WOKAPI0002E": _("Delete is not allowed for %(resource)s"),
    "WOKAPI0003E": _("%(resource)s does not implement update method"),
    "WOKAPI0005E": _("Create is not allowed for %(resource)s"),
    "WOKAPI0006E": _("Unable to parse JSON request"),
    "WOKAPI0007E": _("This API only supports JSON"),
    "WOKAPI0008E": _("Parameters does not match requirement in schema: %(err)s"),
    "WOKAPI0009E": _("You don't have permission to perform this operation."),

    "WOKASYNC0001E": _("Datastore is not initiated in the model object."),
    "WOKASYNC0002E": _("Unable to start task due error: %(err)s"),
    "WOKASYNC0003E": _("Timeout of %(seconds)s seconds expired while running task '%(task)s."),

    "WOKAUTH0001E": _("Authentication failed for user '%(username)s'. [Error code: %(code)s]"),
    "WOKAUTH0002E": _("You are not authorized to access Kimchi"),
    "WOKAUTH0003E": _("Specify %(item)s to login into Kimchi"),
    "WOKAUTH0005E": _("Invalid LDAP configuration: %(item)s : %(value)s"),

    "WOKLOG0001E": _("Invalid filter parameter. Filter parameters allowed: %(filters)s"),
    "WOKLOG0002E": _("Creation of log file failed: %(err)s"),

    "WOKNOT0001E": _("Unable to find notification %(id)s"),
    "WOKNOT0002E": _("Unable to delete notification %(id)s: %(message)s"),

    "WOKOBJST0001E": _("Unable to find %(item)s in datastore"),

    "WOKUTILS0001E": _("Unable to reach %(url)s. Make sure it is accessible and try again."),
    "WOKUTILS0002E": _("Timeout while running command '%(cmd)s' after %(seconds)s seconds"),
    "WOKUTILS0004E": _("Invalid data value '%(value)s'"),
    "WOKUTILS0005E": _("Invalid data unit '%(unit)s'"),

    # These messages (ending with L) are for user log purposes
    "WOKCOL0001L": _("Request made on collection"),
    "WOKRES0001L": _("Request made on resource"),
    "WOKROOT0001L": _("User '%(username)s' login"),
    "WOKROOT0002L": _("User '%(username)s' logout"),
}
