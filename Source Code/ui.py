import pynotify

def show_message(this_string):
	pynotify.init("TEST")			#Just an obligation. Nothing more.
	notice=pynotify.Notification("Live Update ",this_string)
	notice.show()
