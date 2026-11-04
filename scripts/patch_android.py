#!/usr/bin/env python3
"""Chạy trong GitHub Actions sau `npx cap add android`: thêm quyền Bluetooth, khóa ký cố định, số phiên bản."""
import re, sys, pathlib

root = pathlib.Path('android/app')
man = root / 'src/main/AndroidManifest.xml'
t = man.read_text(encoding='utf-8')
if 'xmlns:tools' not in t:
    t = t.replace('<manifest xmlns:android="http://schemas.android.com/apk/res/android"',
                  '<manifest xmlns:android="http://schemas.android.com/apk/res/android" xmlns:tools="http://schemas.android.com/tools"', 1)
assert 'xmlns:tools' in t, 'không thêm được xmlns:tools vào AndroidManifest.xml'
perm = '''
    <!-- Bluetooth cho Android 12+ (không dùng để dò vị trí) và Android 11 trở xuống -->
    <uses-permission android:name="android.permission.BLUETOOTH_SCAN" android:usesPermissionFlags="neverForLocation" tools:targetApi="s" />
    <uses-permission android:name="android.permission.BLUETOOTH_CONNECT" />
    <uses-permission android:name="android.permission.BLUETOOTH" android:maxSdkVersion="30" />
    <uses-permission android:name="android.permission.BLUETOOTH_ADMIN" android:maxSdkVersion="30" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" android:maxSdkVersion="30" />
    <uses-feature android:name="android.hardware.bluetooth_le" android:required="true" />
'''
if 'BLUETOOTH_SCAN' not in t:
    assert '</manifest>' in t
    t = t.replace('</manifest>', perm + '</manifest>', 1)
man.write_text(t, encoding='utf-8')

gr = root / 'build.gradle'
g = gr.read_text(encoding='utf-8')
g += '''

// ---- thêm bởi scripts/patch_android.py ----
android {
    defaultConfig {
        versionCode (System.getenv('VERSION_CODE') ?: '1').toInteger()
        versionName "1.0." + (System.getenv('VERSION_CODE') ?: '1')
    }
    signingConfigs {
        release {
            storeFile file(System.getenv('KS_PATH'))
            storePassword 'hubcontrol'
            keyAlias 'hub'
            keyPassword 'hubcontrol'
        }
    }
    buildTypes {
        release { signingConfig signingConfigs.release }
    }
    lint { abortOnError false; checkReleaseBuilds false }
}
'''
gr.write_text(g, encoding='utf-8')
print('patch OK')
