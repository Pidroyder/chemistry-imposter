[app]
title = Chemistry Imposter
package.name = chemistryimposter
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0
requirements = python3,kivy,kivymd,materialyoucolor,exceptiongroup,asyncgui,asynckivy

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
p4a.branch = master

# Отключаем запрос разрешений, если они не нужны (для вашего приложения)
android.permissions = 

# Фильтр для сборки (чтобы не тянуть лишнее)
android.accept_sdk_license = True
