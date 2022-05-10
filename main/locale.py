from main.api import Translate

manual = {
  "Subscribe to our mails":["Subscribe to our mails" , "हमारे मेल की सदस्यता लें"],
  "Welcome to Sahayata Portal":["Welcome to Sahayata Portal","सहायता पोर्टल में आपका स्वागत है"],
  "Click on the appropriate category:":["Click on the appropriate category:","उपयुक्त श्रेणी पर क्लिक करें:"],
  "Students":["Students","छात्र"],
  "Labourers":["Labourers","मजदूरों"],
  "Employment Schemes":["Employment Schemes","रोजगार योजनाएं"],
  "Social Welfare Schemes":["Social Welfare Schemes","समाज कल्याण योजनाएं"],
  "Women":["Women","औरत"],
  "Subscribe for all latest updates!":["Subscribe for all latest updates!","सभी नवीनतम अपडेट के लिए सदस्यता लें!"],
  "Language":["Language","भाषा"],
  "Our Team":["Our Team","हमारी टीम"],
  "About":["About","हमारे बारे में"],
  "Home":["Home","घर"],
  "National Scholarships":["National Scholarships","राष्ट्रीय छात्रवृत्ति"],
  "International Scholarships":["International Scholarships","अंतर्राष्ट्रीय छात्रवृत्ति"],
  "All Rights Reserved © CP301_G1 2022":["All Rights Reserved © CP301_G1 2022","सर्वाधिकार सुरक्षित © CP301_G1 2022"],
  "Click Here":["Click Here","यहाँ क्लिक करें"],
  "SPEAK":["SPEAK","बोलना"],
  "Click here to know more":["Click here to know more","अधिक जानकारी के लिए यहां क्लिक करें"],
  "Loading":["Loading","प्रतीक्षा करें"],
  "OTP":["OTP","ओटीपी"],
  "About | Sahayata Portal":["About | Sahayata Portal","हमारे बारे में | सहायता पोर्टल"],
  "Employment Schemes | Sahayata Portal":["Employment Schemes | Sahayata Portal","रोजगार योजनाएं | सहायता पोर्टल"],
  "Home | Sahayata Portal":["Home | Sahayata Portal","होमपेज | सहायता पोर्टल"],
  "Our Team | Sahayata Portal":["Our Team | Sahayata Portal","हमारी टीम | सहायता पोर्टल"],
  "Schemes | Sahayata Portal":["Schemes | Sahayata Portal","योजनाएं | सहायता पोर्टल"],
  "Scholarships | Sahayata Portal":["Scholarships | Sahayata Portal","छात्रवृत्ति | सहायता पोर्टल"],
  "Social Welfare Schemes | Sahayata Portal":["Social Welfare Schemes | Sahayata Portal","समाज कल्याण योजनाएं | सहायता पोर्टल"],
  "Subscribe | Sahayata Portal":["Subscribe | Sahayata Portal","सदस्यता लें | सहायता पोर्टल"],
  "Unsubscribe | Sahayata Portal":["Unsubscribe | Sahayata Portal","सदस्यता छोड़ें | सहायता पोर्टल"],
  "Schemes for women | Sahayata Portal":["Schemes for women | Sahayata Portal","महिलाओं के लिए योजनाएं | सहायता पोर्टल"],
}

def trans(text, lang):
  try:
    temp = manual[text]
    if lang=="en":
      return temp[0]
    elif lang=="hi":
      return temp[1]
  except:
    pass
  

  return Translate(text, lang)