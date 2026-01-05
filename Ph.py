"""
📿 سكربت الصلاة على النبي محمد ﷺ
🎨 واجهة ملونة مع مميزات متنوعة
"""

import time
import os
import random
from datetime import datetime

class Colors:
    """ألوان ANSI للطباعة"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def clear_screen():
    """مسح الشاشة"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """عرض بانر جميل"""
    banner = f"""
{Colors.PURPLE}{'='*60}{Colors.END}
{Colors.YELLOW}{Colors.BOLD}            📿 سكربت الصلاة على النبي محمد ﷺ 📿{Colors.END}
{Colors.CYAN}              قال تعالى: {Colors.END}
{Colors.GREEN}    ﴿إِنَّ اللَّهَ وَمَلَائِكَتَهُ يُصَلُّونَ عَلَى النَّبِيِّ{Colors.END}
{Colors.GREEN}     يَا أَيُّهَا الَّذِينَ آمَنُوا صَلُّوا عَلَيْهِ{Colors.END}
{Colors.GREEN}         وَسَلِّمُوا تَسْلِيمًا﴾ [الأحزاب: 56]{Colors.END}
{Colors.PURPLE}{'='*60}{Colors.END}
    """
    print(banner)

def salah_ala_nabi_arabic():
    """الصيغ العربية للصلاة على النبي"""
    prayers = [
        "اللَّهُمَّ صَلِّ عَلَى مُحَمَّدٍ وَعَلَى آلِ مُحَمَّدٍ، كَمَا صَلَّيْتَ عَلَى إِبْرَاهِيمَ وَعَلَى آلِ إِبْرَاهِيمَ، إِنَّكَ حَمِيدٌ مَجِيدٌ، اللَّهُمَّ بَارِكْ عَلَى مُحَمَّدٍ وَعَلَى آلِ مُحَمَّدٍ، كَمَا بَارَكْتَ عَلَى إِبْرَاهِيمَ وَعَلَى آلِ إِبْرَاهِيمَ، إِنَّكَ حَمِيدٌ مَجِيدٌ",
        
        "اللهم صل على محمد وعلى آل محمد كما صليت على إبراهيم وعلى آل إبراهيم وبارك على محمد وعلى آل محمد كما باركت على إبراهيم وعلى آل إبراهيم في العالمين إنك حميد مجيد",
        
        "صلى الله على محمد، صلى الله عليه وسلم",
        
        "اللهم صل وسلم وبارك على سيدنا محمد وعلى آله وصحبه أجمعين",
        
        "اللهم صل على محمد النبي الأمي، وعلى آل محمد، وبارك على محمد النبي الأمي، وعلى آل محمد، كما صليت وباركت على إبراهيم وعلى آل إبراهيم، إنك حميد مجيد",
        
        "اللهم صل على محمد عبدك ورسولك كما صليت على إبراهيم، وبارك على محمد وعلى آل محمد كما باركت على إبراهيم وعلى آل إبراهيم",
        
        "اللهم صل على محمد وعلى أزواجه وذريته كما صليت على آل إبراهيم، وبارك على محمد وعلى أزواجه وذريته كما باركت على آل إبراهيم، إنك حميد مجيد",
    ]
    return prayers

def salah_ala_nabi_phonetic():
    """الصلاة على النبي مع النطق الصوتي"""
    prayers = [
        "Allahumma salli 'ala Muhammadin wa 'ala ali Muhammadin, kama sallayta 'ala Ibrahima wa 'ala ali Ibrahima, innaka hamidum majid. Allahumma barik 'ala Muhammadin wa 'ala ali Muhammadin, kama barakta 'ala Ibrahima wa 'ala ali Ibrahima, innaka hamidum majid.",
        
        "Salla Allahu 'alayhi wa sallam",
        
        "Allahumma salli wa sallim wa barik 'ala sayyidina Muhammadin wa 'ala alihi wa sahbihi ajma'een",
    ]
    return prayers

def print_with_animation(text, delay=0.05):
    """طباعة النص بحركة"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def counter_salah():
    """عداد للصلاة على النبي"""
    print(f"\n{Colors.CYAN}{Colors.BOLD}🧮 عداد الصلاة على النبي ﷺ{Colors.END}")
    print(f"{Colors.WHITE}{'='*40}{Colors.END}")
    
    try:
        count = int(input(f"{Colors.YELLOW}كم مرة تريد الصلاة على النبي؟ {Colors.END}"))
        
        if count <= 0:
            print(f"{Colors.RED}⚠️ أدخل رقم أكبر من الصفر{Colors.END}")
            return
        
        prayer = salah_ala_nabi_arabic()[0]
        
        print(f"\n{Colors.GREEN}🚀 ابدأ بالصلاة...{Colors.END}")
        print(f"{Colors.WHITE}{'='*40}{Colors.END}\n")
        
        for i in range(1, count + 1):
            print(f"{Colors.BLUE}{i:3}. {Colors.END}", end="")
            print_with_animation(f"{Colors.GREEN}{prayer}{Colors.END}", 0.01)
            
            if i % 10 == 0:
                print(f"{Colors.YELLOW}✨ أكملت {i} صلاة! تابع...{Colors.END}\n")
            
            time.sleep(0.5)
        
        print(f"\n{Colors.PURPLE}{'='*40}{Colors.END}")
        print(f"{Colors.CYAN}{Colors.BOLD}🎉 مبروك! لقد صليت على النبي ﷺ {count} مرة{Colors.END}")
        
        # فضل الصلاة
        print(f"\n{Colors.YELLOW}📖 فضل الصلاة على النبي:{Colors.END}")
        print(f"{Colors.WHITE}• من صلى على النبي مرة صلى الله عليه بها عشرًا{Colors.END}")
        print(f"{Colors.WHITE}• ترفع الدرجات وتكفر السيئات{Colors.END}")
        print(f"{Colors.WHITE}• تقضي الحاجات وتفرج الكربات{Colors.END}")
        
    except ValueError:
        print(f"{Colors.RED}⚠️ أدخل رقم صحيح!{Colors.END}")

def random_salah():
    """صلاة عشوائية مع معلومات"""
    print(f"\n{Colors.PURPLE}{Colors.BOLD}🎲 صلاة عشوائية على النبي ﷺ{Colors.END}")
    
    arabic_prayers = salah_ala_nabi_arabic()
    phonetic_prayers = salah_ala_nabi_phonetic()
    
    # اختيار عشوائي
    arabic = random.choice(arabic_prayers)
    phonetic = random.choice(phonetic_prayers)
    
    print(f"\n{Colors.CYAN}📿 الصيغة العربية:{Colors.END}")
    print(f"{Colors.GREEN}{arabic}{Colors.END}")
    
    print(f"\n{Colors.YELLOW}🔤 النطق الصوتي:{Colors.END}")
    print(f"{Colors.WHITE}{phonetic}{Colors.END}")
    
    # معلومات عن الصيغة
    print(f"\n{Colors.BLUE}📚 معلومات:{Colors.END}")
    print(f"{Colors.WHITE}• عدد الكلمات: {len(arabic.split())}{Colors.END}")
    print(f"{Colors.WHITE}• عدد الأحرف: {len(arabic)}{Colors.END}")

def salah_with_meaning():
    """الصلاة على النبي مع شرح المعنى"""
    print(f"\n{Colors.BLUE}{Colors.BOLD}📖 الصلاة على النبي مع المعنى{Colors.END}")
    
    prayer = "اللهم صل على محمد وعلى آل محمد كما صليت على إبراهيم وعلى آل إبراهيم وبارك على محمد وعلى آل محمد كما باركت على إبراهيم وعلى آل إبراهيم في العالمين إنك حميد مجيد"
    
    print(f"\n{Colors.GREEN}📿 الصيغة:{Colors.END}")
    print(f"{Colors.CYAN}{prayer}{Colors.END}")
    
    print(f"\n{Colors.YELLOW}🎯 معنى الصلاة:{Colors.END}")
    meanings = [
        "اللهم: يا الله",
        "صل: أنزل الرحمة والثناء الجميل",
        "على محمد: النبي ﷺ",
        "وعلى آل محمد: أهل بيته وأتباعه",
        "كما صليت على إبراهيم: بنفس الكيفية التي أنزلتها على إبراهيم",
        "إنك حميد مجيد: أنت المحمود المجيد"
    ]
    
    for meaning in meanings:
        print(f"{Colors.WHITE}• {meaning}{Colors.END}")
        time.sleep(0.5)

def daily_reminder():
    """مذكر يومي للصلاة على النبي"""
    print(f"\n{Colors.GREEN}{Colors.Bold}⏰ مذكر الصلاة اليومي{Colors.END}")
    
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    print(f"{Colors.WHITE}📅 التاريخ: {current_date}{Colors.END}")
    print(f"{Colors.WHITE}⏰ الوقت: {current_time}{Colors.END}")
    
    # اقتراح أوقات للصلاة
    print(f"\n{Colors.YELLOW}🕰️ أوقات مستحبة للصلاة على النبي:{Colors.END}")
    times = [
        "بعد كل أذان",
        "يوم الجمعة",
        "عند الدعاء",
        "قبل النوم",
        "عند الاستيقاظ",
        "عند ذكر اسم النبي ﷺ"
    ]
    
    for i, time_sugg in enumerate(times, 1):
        print(f"{Colors.WHITE}{i}. {time_sugg}{Colors.END}")
    
    # عدد الصلوات اليومية المستحبة
    print(f"\n{Colors.CYAN}🎯 الهدف اليومي:{Colors.END}")
    print(f"{Colors.WHITE}حاول أن تصلي على النبي ﷺ 100 مرة يوميًا{Colors.END}")
    print(f"{Colors.WHITE}قال ﷺ: 'من صلى علي صلاة صلى الله عليه بها عشرًا'{Colors.END}")

def benefits_of_salah():
    """فوائد الصلاة على النبي"""
    print(f"\n{Colors.RED}{Colors.BOLD}✨ فوائد الصلاة على النبي محمد ﷺ{Colors.END}")
    
    benefits = [
        "1. ✅ طاعة لأمر الله تعالى",
        "2. ✅ سبب لمغفرة الذنوب",
        "3. ✅ سبب لرفع الدرجات",
        "4. ✅ سبب لقضاء الحوائج",
        "5. ✅ سبب لشفاعة النبي ﷺ",
        "6. ✅ سبب للبركة في الرزق",
        "7. ✅ سبب للنجاة من الشدائد",
        "8. ✅ سبب للفرج والتفريج",
        "9. ✅ سبب لاستجابة الدعاء",
        "10. ✅ سبب لزيادة الحسنات"
    ]
    
    for benefit in benefits:
        print(f"{Colors.GREEN}{benefit}{Colors.END}")
        time.sleep(0.3)

def interactive_menu():
    """القائمة التفاعلية"""
    while True:
        clear_screen()
        print_banner()
        
        print(f"\n{Colors.CYAN}{Colors.BOLD}📋 القائمة الرئيسية:{Colors.END}")
        print(f"{Colors.WHITE}{'='*50}{Colors.END}")
        print(f"{Colors.YELLOW}1. 🧮 عداد الصلاة على النبي{Colors.END}")
        print(f"{Colors.YELLOW}2. 🎲 صلاة عشوائية{Colors.END}")
        print(f"{Colors.YELLOW}3. 📖 الصلاة مع المعنى{Colors.END}")
        print(f"{Colors.YELLOW}4. ⏰ المذكر اليومي{Colors.END}")
        print(f"{Colors.YELLOW}5. ✨ فوائد الصلاة على النبي{Colors.END}")
        print(f"{Colors.YELLOW}6. 📜 جميع صيغ الصلاة{Colors.END}")
        print(f"{Colors.YELLOW}7. 💾 حفظ الصلوات{Colors.END}")
        print(f"{Colors.YELLOW}0. 🚪 خروج{Colors.END}")
        print(f"{Colors.WHITE}{'='*50}{Colors.END}")
        
        choice = input(f"\n{Colors.GREEN}🔸 اختر رقم (0-7): {Colors.END}")
        
        if choice == "1":
            counter_salah()
            input(f"\n{Colors.CYAN}اضغط Enter للعودة...{Colors.END}")
            
        elif choice == "2":
            random_salah()
            input(f"\n{Colors.CYAN}اضغط Enter للعودة...{Colors.END}")
            
        elif choice == "3":
            salah_with_meaning()
            input(f"\n{Colors.CYAN}اضغط Enter للعودة...{Colors.END}")
            
        elif choice == "4":
            daily_reminder()
            input(f"\n{Colors.CYAN}اضغط Enter للعودة...{Colors.END}")
            
        elif choice == "5":
            benefits_of_salah()
            input(f"\n{Colors.CYAN}اضغط Enter للعودة...{Colors.END}")
            
        elif choice == "6":
            show_all_prayers()
            input(f"\n{Colors.CYAN}اضغط Enter للعودة...{Colors.END}")
            
        elif choice == "7":
            save_prayers_to_file()
            input(f"\n{Colors.CYAN}اضغط Enter للعودة...{Colors.END}")
            
        elif choice == "0":
            print(f"\n{Colors.GREEN}🎉 جزاك الله خيرًا على صلاتك على النبي ﷺ{Colors.END}")
            print(f"{Colors.BLUE}👋 إلى اللقاء...{Colors.END}")
            break
            
        else:
            print(f"{Colors.RED}⚠️ اختر رقم صحيح من 0 إلى 7{Colors.END}")
            time.sleep(1)

def show_all_prayers():
    """عرض جميع صيغ الصلاة"""
    print(f"\n{Colors.BLUE}{Colors.BOLD}📜 جميع صيغ الصلاة على النبي ﷺ{Colors.END}")
    
    arabic_prayers = salah_ala_nabi_arabic()
    phonetic_prayers = salah_ala_nabi_phonetic()
    
    print(f"\n{Colors.GREEN}📖 الصيغ العربية:{Colors.END}")
    for i, prayer in enumerate(arabic_prayers, 1):
        print(f"\n{Colors.CYAN}{i}. {Colors.END}{prayer}")
        time.sleep(0.3)
    
    print(f"\n{Colors.YELLOW}🔤 الصيغ الصوتية:{Colors.END}")
    for i, prayer in enumerate(phonetic_prayers, 1):
        print(f"\n{Colors.WHITE}{i}. {Colors.END}{prayer}")

def save_prayers_to_file():
    """حفظ الصلوات في ملف"""
    filename = "صلاة_على_النبي.txt"
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("="*60 + "\n")
        file.write("صيغ الصلاة على النبي محمد ﷺ\n")
        file.write("="*60 + "\n\n")
        
        file.write("📖 الصيغ العربية:\n")
        file.write("-"*40 + "\n")
        for i, prayer in enumerate(salah_ala_nabi_arabic(), 1):
            file.write(f"{i}. {prayer}\n\n")
        
        file.write("\n🔤 الصيغ الصوتية:\n")
        file.write("-"*40 + "\n")
        for i, prayer in enumerate(salah_ala_nabi_phonetic(), 1):
            file.write(f"{i}. {prayer}\n\n")
        
        file.write("\n" + "="*60 + "\n")
        file.write("جزاك الله خيرًا على صلاتك على النبي ﷺ\n")
        file.write(f"تم الإنشاء في: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write("="*60)
    
    print(f"\n{Colors.GREEN}✅ تم حفظ الصلوات في ملف: {filename}{Colors.END}")

def main():
    """الدالة الرئيسية"""
    try:
        clear_screen()
        interactive_menu()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}⚠️ تم إيقاف البرنامج{Colors.END}")
        print(f"{Colors.BLUE}📿 لا تنس الصلاة على النبي ﷺ{Colors.END}")

if __name__ == "__main__":
    main()
