import harfang as hg

hg.InputInit()
hg.WindowSystemInit()

win = hg.RenderInit(400, 300, hg.RF_None)

while not hg.ReadKeyboard().Key(hg.K_Escape):
	hg.SetViewRect(0, 0, 0, 400, 300)
	hg.SetViewClear(0, hg.CF_Color, hg.RGBA32(96, 32, 255))

	hg.Touch(0)

	hg.Frame()
	hg.UpdateWindow(win)

hg.DestroyWindow(win)