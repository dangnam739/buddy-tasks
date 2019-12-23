#Yêu cầu: class Gintent trong file detect.py có hàm xử lý intent_of():
- class sẽ load một model fasttext
- Đầu vào là một câu dạng string
- Đầu ra là intent của câu đó, cũng ở dạng string.
#Cách đặt tên intent phụ thuộc vào data mà người làm tự chuẩn bị.

#Ví dụ: 
```python
from detect import Gintent
MODEL_PATH = "somewhere/tp/model.bin"

gintent = Gintent(MODEL_PATH)
intent = gintent.intent_of("Xin chao cac ban!)
print(intent)
```  
Khi in ra ta được  
```bash
"__chaohoi__"
```  
 Task:
 - Xây dựng hàm intent_of thỏa mãn yêu cầu trên (làm kiểu gì cũng được)
