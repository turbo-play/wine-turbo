@ stdcall -private DllCanUnloadNow()
@ stdcall -private DllGetClassObject(ptr ptr ptr)
@ stdcall -private DllRegisterServer()
@ stdcall -private DllUnregisterServer()
@ stub DockPattern_SetDockPosition
@ stub ExpandCollapsePattern_Collapse
@ stub ExpandCollapsePattern_Expand
@ stub GridPattern_GetItem
#@ stub IgnoreLeaksInCurrentlyTrackedMemory
@ stub InvokePattern_Invoke
@ stub ItemContainerPattern_FindItemByProperty
@ stub LegacyIAccessiblePattern_DoDefaultAction
@ stub LegacyIAccessiblePattern_GetIAccessible
@ stub LegacyIAccessiblePattern_Select
@ stub LegacyIAccessiblePattern_SetValue
@ stub MultipleViewPattern_GetViewName
@ stub MultipleViewPattern_SetCurrentView
#@ stub PostTestCheckForLeaks
@ stub RangeValuePattern_SetValue
@ stub ScrollItemPattern_ScrollIntoView
@ stub ScrollPattern_Scroll
@ stub ScrollPattern_SetScrollPercent
@ stub SelectionItemPattern_AddToSelection
@ stub SelectionItemPattern_RemoveFromSelection
@ stub SelectionItemPattern_Select
@ stub SynchronizedInputPattern_Cancel
@ stub SynchronizedInputPattern_StartListening
@ stub TextPattern_GetSelection
@ stub TextPattern_GetVisibleRanges
@ stub TextPattern_RangeFromChild
@ stub TextPattern_RangeFromPoint
@ stub TextPattern_get_DocumentRange
@ stub TextPattern_get_SupportedTextSelection
@ stub TextRange_AddToSelection
@ stub TextRange_Clone
@ stub TextRange_Compare
@ stub TextRange_CompareEndpoints
@ stub TextRange_ExpandToEnclosingUnit
@ stub TextRange_FindAttribute
@ stub TextRange_FindText
@ stub TextRange_GetAttributeValue
@ stub TextRange_GetBoundingRectangles
@ stub TextRange_GetChildren
@ stub TextRange_GetEnclosingElement
@ stub TextRange_GetText
@ stub TextRange_Move
@ stub TextRange_MoveEndpointByRange
@ stub TextRange_MoveEndpointByUnit
@ stub TextRange_RemoveFromSelection
@ stub TextRange_ScrollIntoView
@ stub TextRange_Select
@ stub TogglePattern_Toggle
@ stub TransformPattern_Move
@ stub TransformPattern_Resize
@ stub TransformPattern_Rotate
@ stub UiaAddEvent
@ stdcall UiaClientsAreListening()
#@ stub UiaDisconnectAllProviders
#@ stub UiaDisconnectProvider
@ stub UiaEventAddWindow
@ stub UiaEventRemoveWindow
@ stub UiaFind
@ stub UiaGetErrorDescription
@ stub UiaGetPatternProvider
@ stub UiaGetPropertyValue
@ stdcall UiaGetReservedMixedAttributeValue(ptr)
@ stdcall UiaGetReservedNotSupportedValue(ptr)
@ stub UiaGetRootNode
@ stub UiaGetRuntimeId
@ stub UiaGetUpdatedCache
@ stub UiaHPatternObjectFromVariant
@ stub UiaHTextRangeFromVariant
@ stub UiaHUiaNodeFromVariant
@ stub UiaHasServerSideProvider
@ stdcall UiaHostProviderFromHwnd(long ptr)
#@ stub UiaIAccessibleFromProvider
@ stdcall UiaLookupId(long ptr)
@ stub UiaNavigate
@ stub UiaNodeFromFocus
@ stub UiaNodeFromHandle
@ stub UiaNodeFromPoint
@ stub UiaNodeFromProvider
@ stub UiaNodeRelease
@ stub UiaPatternRelease
#@ stub UiaProviderForNonClient
#@ stub UiaProviderFromIAccessible
@ stdcall UiaRaiseAsyncContentLoadedEvent(ptr long double)
@ stdcall UiaRaiseAutomationEvent(ptr long)
@ stdcall UiaRaiseAutomationPropertyChangedEvent(ptr long int128 int128)
@ stdcall UiaRaiseChangesEvent(ptr long ptr)
@ stdcall UiaRaiseNotificationEvent(ptr long long wstr wstr)
@ stdcall UiaRaiseStructureChangedEvent(ptr long ptr long)
@ stdcall UiaRaiseTextEditTextChangedEvent(ptr long ptr)
@ stdcall UiaRegisterProviderCallback(ptr)
@ stub UiaRemoveEvent
@ stdcall UiaReturnRawElementProvider(long long long ptr)
@ stub UiaSetFocus
@ stub UiaTextRangeRelease
#@ stub UpdateErrorLoggingCallback
@ stub ValuePattern_SetValue
@ stub VirtualizedItemPattern_Realize
@ stub WindowPattern_Close
@ stub WindowPattern_SetWindowVisualState
@ stub WindowPattern_WaitForInputIdle
