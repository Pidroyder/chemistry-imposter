[app]
title = Химический шпион
package.name = chemistryimposter
package.domain = com.chemistryimposter

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0
requirements = python3,kivy,kivymd,materialyoucolor,exceptiongroup,asyncgui,asynckivy

orientation = portrait
fullscreen = 0

icon.filename = ../images/icon.png
presplash.filename = ../images/icon.jpg
android.presplash_color = #000000

android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
p4a.branch = master

android.permissions = 

android.accept_sdk_license = True
