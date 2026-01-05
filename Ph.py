# run_from_github.py
"""
سكريبت لتشغيل سكريبت آخر من GitHub
"""

import requests
import sys
import os
from datetime import datetime

def clear_screen():
    """مسح الشاشة"""
    os.system('clear' if os.name == 'posix' else 'cls')

def download_and_run(url, filename="downloaded_script.py"):
    """
    تحميل وتشغيل سكريبت من الإنترنت
    """
    print(f"🔍 جاري تحميل السكريبت من: {url}")
    print("⏳ يرجى الانتظار...")
    
    try:
        # تحميل السكريبت
        response = requests.get(url)
        response.raise_for_status()  # التحقق من عدم وجود أخطاء
        
        # حفظ الملف مؤقتاً
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        print(f"✅ تم التحميل بنجاح!")
        print(f"📁 تم الحفظ في: {filename}")
        print(f"📊 حجم الملف: {len(response.text)} حرف")
        
        # عرض جزء من الكود
        print("\n📝 جزء من الكود:")
        lines = response.text.split('\n')[:10]
        for i, line in enumerate(lines, 1):
            print(f"{i:3}: {line}")
        
        # سؤال المستخدم
        print("\n" + "="*50)
        choice = input("🔸 هل تريد تشغيل السكريبت الآن؟ (y/n): ")
        
        if choice.lower() == 'y':
            print("▶️ جاري تشغيل السكريبت...")
            print("="*50 + "\n")
            
            # تنفيذ السكريبت
            with open(filename, 'r', encoding='utf-8') as f:
                script_code = f.read()
            
            # إنشاء بيئة تنفيذ
            exec_globals = {
                '__name__': '__main__',
                '__file__': filename,
                'requests': requests,
                'datetime': datetime
            }
            
            # تنفيذ الكود
            exec(script_code, exec_globals)
            
        else:
            print("📁 يمكنك تشغيل الملف لاحقاً:")
            print(f"📱 اسم الملف: {filename}")
        
        # تنظيف (اختياري)
        cleanup = input("\n🔸 هل تريد حذف الملف بعد التشغيل؟ (y/n): ")
        if cleanup.lower() == 'y':
            os.remove(filename)
            print("🗑️ تم حذف الملف المؤقت")
        
    except requests.exceptions.ConnectionError:
        print("❌ خطأ في الاتصال بالإنترنت!")
        print("🔸 تأكد من اتصالك بالإنترنت")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ خطأ في تحميل السكريبت: {e}")
        
    except Exception as e:
        print(f"❌ حدث خطأ غير متوقع: {e}")
        import traceback
        traceback.print_exc()

def main():
    """الدالة الرئيسية"""
    clear_screen()
    
    print("🎯" + "="*48 + "🎯")
    print("      🚀 مُشَغِّل سَكْرِبْتَات مِن GitHub")
    print("🎯" + "="*48 + "🎯")
    
    print("\n📋 الخيارات المتاحة:")
    print("1. تشغيل سكريبت الآلة الحاسبة (مثال)")
    print("2. إدخال رابط مخصص")
    print("3. الخروج")
    
    choice = input("\n🔸 اختر خياراً (1-3): ")
    
    if choice == '1':
        # رابط السكريبت المثال على GitHub
        # استبدل هذا برابطك الحقيقي بعد رفعه
        url = "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/calculator.py"
        print(f"\n🔗 الرابط الافتراضي: {url}")
        
        # يمكن للمستخدم تعديل الرابط
        custom = input("🔸 هل تريد استخدام رابط آخر؟ (y/n): ")
        if custom.lower() == 'y':
            url = input("🔗 أدخل الرابط الكامل للسكريبت: ")
        
        download_and_run(url, "calculator_from_github.py")
        
    elif choice == '2':
        url = input("\n🔗 أدخل الرابط الكامل للسكريبت (Raw URL): ")
        
        if not url.startswith('http'):
            print("❌ الرابط غير صالح!")
            return
        
        filename = input("📁 اسم الملف المحفوظ (اختياري): ")
        if not filename:
            filename = "github_script.py"
        
        download_and_run(url, filename)
        
    elif choice == '3':
        print("\n👋 إلى اللقاء!")
        sys.exit(0)
        
    else:
        print("❌ اختر خياراً صحيحاً!")

if __name__ == "__main__":
    # تثبيت requests إذا لم يكن مثبتاً
    try:
        import requests
    except ImportError:
        print("📦 جاري تثبيت حزمة requests...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
        import requests
    
    main()
