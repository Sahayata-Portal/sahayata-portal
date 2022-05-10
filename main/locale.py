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