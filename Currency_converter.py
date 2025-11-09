### بداية الملف: currency_converter.py ###
import requests
from datetime import datetime

def جلب_سعر_الدولار():
    try:
        الرابط = "https://lirarate.com/wp-content/themes/lirarate/include/ajax.php?currencies=USD"
        الاستجابة = requests.get(الرابط, timeout=10)
        البيانات = الاستجابة.json()
        السعر = float(البيانات['currencies']['USD']['buy'])
        return السعر
    except:
        return 15100  # سعر احتياطي إذا النت مقطوع

def تحويل_دولار_لليرة(دولار):
    السعر = جلب_سعر_الدولار()
    return int(دولار * السعر)

print("=== أ warm welcome من أداة تحويل العملات السورية ===")
print(f"التاريخ والوقت: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print(f"سعر الدولار اليوم: {جلب_سعر_الدولار():,} ليرة سورية")

while True:
    try:
        دولار = float(input("\nكم دولار بدك تحول؟ (اكتب 0 للخروج): "))
        if دولار == 0:
            print("شكراً كتير يا بطل! نشوفك على خير")
            break
        ليرة = تحويل_دولار_لليرة(دولار)
        print(f"{دولار} دولار = {ليرة:,} ليرة سورية")
    except:
        print("يا زلمة اكتب رقم صحيح! جرب مرة تانية")
### نهاية الملف ###
