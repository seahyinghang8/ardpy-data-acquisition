# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class FrameMain
###########################################################################

class FrameMain ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Research Is Awesome", pos = wx.DefaultPosition, size = wx.Size( 800,345 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        SizerFrame = wx.BoxSizer( wx.VERTICAL )
        
        self.MainPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        SizerPanel = wx.BoxSizer( wx.VERTICAL )
        
        SizerPanel.SetMinSize( wx.Size( 800,-1 ) ) 
        self.filePicker1 = wx.FilePickerCtrl( self.MainPanel, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( 800,-1 ), wx.FLP_DEFAULT_STYLE )
        self.filePicker1.Enable( False )
        
        SizerPanel.Add( self.filePicker1, 0, wx.ALL, 5 )
        
        self.text2 = wx.StaticText( self.MainPanel, wx.ID_ANY, u"Remarks", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.text2.Wrap( -1 )
        SizerPanel.Add( self.text2, 0, wx.ALL, 5 )
        
        self.input1 = wx.TextCtrl( self.MainPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 800,-1 ), 0 )
        SizerPanel.Add( self.input1, 0, wx.ALL, 5 )
        
        self.input2 = wx.TextCtrl( self.MainPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 800,-1 ), wx.TE_MULTILINE )
        SizerPanel.Add( self.input2, 0, wx.ALL, 5 )
        
        self.input3 = wx.TextCtrl( self.MainPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 800,-1 ), 0 )
        SizerPanel.Add( self.input3, 0, wx.ALL, 5 )
        
        SizerBottom1 = wx.BoxSizer( wx.HORIZONTAL )
        
        SizerBottom2 = wx.BoxSizer( wx.VERTICAL )
        
        self.text3 = wx.StaticText( self.MainPanel, wx.ID_ANY, u"No. of Charts", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.text3.Wrap( -1 )
        SizerBottom2.Add( self.text3, 0, wx.ALL, 5 )
        
        choice1Choices = [ u"1", u"2", u"3", u"4" ]
        self.choice1 = wx.Choice( self.MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), choice1Choices, 0 )
        self.choice1.SetSelection( 0 )
        SizerBottom2.Add( self.choice1, 0, wx.ALL, 5 )
        
        SizerButton = wx.BoxSizer( wx.HORIZONTAL )
        
        self.button1 = wx.Button( self.MainPanel, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
        SizerButton.Add( self.button1, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
        
        self.button2 = wx.Button( self.MainPanel, wx.ID_ANY, u"End", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.button2.Enable( False )
        
        SizerButton.Add( self.button2, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
        
        
        SizerBottom2.Add( SizerButton, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        SizerBottom1.Add( SizerBottom2, 1, wx.EXPAND, 5 )
        
        self.text1 = wx.StaticText( self.MainPanel, wx.ID_ANY, u"Instructions:\n1. Type all required info in remarks\n2. Select number of data charts to display\n3. Click \"Start\" and type in the name for the data file\n4. Leave the charts open until experiments end\n5. Click \"End\" to save the remarks and conclude experiment\n6. Restart data acquistion or close application", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.text1.Wrap( -1 )
        SizerBottom1.Add( self.text1, 0, wx.ALL, 5 )
        
        
        SizerPanel.Add( SizerBottom1, 1, wx.EXPAND, 5 )
        
        
        self.MainPanel.SetSizer( SizerPanel )
        self.MainPanel.Layout()
        SizerPanel.Fit( self.MainPanel )
        SizerFrame.Add( self.MainPanel, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( SizerFrame )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.button1.Bind( wx.EVT_BUTTON, self.start )
        self.button2.Bind( wx.EVT_BUTTON, self.end )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def start( self, event ):
        event.Skip()
    
    def end( self, event ):
        event.Skip()