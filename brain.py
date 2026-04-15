import wikipedia
import random
import ast
import operator as op

wikipedia.set_lang("tr")

# -----------------
# KONUSMA TARZI
# -----------------
girisler = [
    "Soyle aciklayayim:",
    "Kisaca:",
    "Basitce:",
    "Ozetle:"
]

# -----------------
# SOHBET DATASET
# -----------------
sohbet = {
    "merhaba": "Merhaba, sana nasil yardimci olabilirim?",
    "selam": "Selam, ne ogrenmek istiyorsun?",
    "nasilsin": "Iyiyim, sen nasilsin?",
    "adin ne": "Ben Nico AI.",
    "tesekkur": "Rica ederim.",
    "bye": "Gorusuruz."
}

# -----------------
# BILGI DATASET
# -----------------
dataset = {
    "python": "Python basit ve guclu bir programlama dilidir.",
    "arduino": "Arduino mikrodenetleyici gelistirme platformudur.",
    "esp32": "ESP32 wifi ve bluetooth destekli bir karttir."
}

# -----------------
# GUVENLI MATEMATIK
# -----------------
operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv
}

def safe_eval(expr):
    def eval_node(node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            return operators[type(node.op)](
                eval_node(node.left),
                eval_node(node.right)
            )
        else:
            raise Exception()

    try:
        node = ast.parse(expr, mode='eval').body
        return eval_node(node)
    except:
        return None

# -----------------
# 5N1K
# -----------------
def analiz_5n1k(msg):
    msg = msg.lower()

    if "nedir" in msg:
        return "Bu su anlama gelir: "
    if "neden" in msg:
        return "Bunun nedeni: "
    if "nasil" in msg:
        return "Bunu soyle yapabilirsin: "
    if "nerede" in msg:
        return "Genelde su ortamda olur: "
    if "ne zaman" in msg:
        return "Zaman olarak: "
    if "kim" in msg:
        return "Bu kisi hakkinda: "

    return ""

# -----------------
# SOHBET
# -----------------
def sohbet_cevap(msg):
    msg = msg.lower()
    for key in sohbet:
        if key in msg:
            return sohbet[key]
    return None

# -----------------
# CODEX (ARDUINO + ESP32)
# -----------------
def codex(msg):
    msg = msg.lower()

    if "arduino" in msg:
        if "led" in msg:
            return """Arduino LED:

void setup() {
  pinMode(13, OUTPUT);
}

void loop() {
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  delay(1000);
}
"""

    if "esp32" in msg:
        if "wifi" in msg:
            return """ESP32 WiFi:

#include <WiFi.h>

const char* ssid = "SSID";
const char* password = "PASSWORD";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }

  Serial.println("Baglandi");
}

void loop() {}
"""

    return None

# -----------------
# DATASET
# -----------------
def dataset_cevap(msg):
    msg = msg.lower()
    for key in dataset:
        if key in msg:
            return dataset[key]
    return None

# -----------------
# WIKIPEDIA
# -----------------
def wiki(msg):
    try:
        return wikipedia.summary(msg, sentences=2)
    except:
        return None

# -----------------
# INSANLASTIR
# -----------------
def insan(text):
    return random.choice(girisler) + " " + text

# -----------------
# ANA SISTEM
# -----------------
def get_response(msg):
    if not msg:
        return "Bir sey yaz."

    # 1 sohbet
    s = sohbet_cevap(msg)
    if s:
        return s

    # 2 codex
    c = codex(msg)
    if c:
        return c

    # 3 matematik
    m = safe_eval(msg)
    if m is not None:
        return "Sonuc: " + str(m)

    # 4 dataset
    d = dataset_cevap(msg)
    if d:
        return insan(analiz_5n1k(msg) + d)

    # 5 wikipedia
    w = wiki(msg)
    if w:
        return insan(analiz_5n1k(msg) + w)

    return "Soruyu daha acik yazarsan yardimci olabilirim."