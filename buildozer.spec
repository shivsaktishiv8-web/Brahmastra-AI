[app]
title = Brahmastra AI
package.name = brahmastra
package.domain = org.panini
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,tflite
version = 0.1
requirements = python3,kivy,kivymd,numpy,pandas,tensorflow-lite
# Permissions jo tune mangi (Location, Offline Messaging)
android.permissions = INTERNET, ACCESS_COARSE_LOCATION, ACCESS_FINE_LOCATION, SEND_SMS, RECEIVE_SMS
orientation = portrait
fullscreen = 1
android.archs = arm64-v8a

