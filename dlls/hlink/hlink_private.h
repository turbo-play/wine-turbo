/*
 * Copyright 2007 Jacek Caban for CodeWeavers
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA
 */

#include <stdarg.h>

#define COBJMACROS

#include "winerror.h"
#include "windef.h"
#include "winbase.h"
#include "winuser.h"
#include "ole2.h"
#include "hlink.h"

extern HRESULT WINAPI HLink_Constructor(IUnknown*,REFIID,void**);
extern HRESULT WINAPI HLinkBrowseContext_Constructor(IUnknown*,REFIID,void**);
