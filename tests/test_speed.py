from util.crf.word_tokenize import word_tokenize
from pyvi import ViTokenizer


text = "Đầu giờ chiều ngày 7/9, trao đổi với Báo Giao thông, ông Nguyễn Ngọc Hùng, Giám đốc Sở Thông tin và Truyền thông tỉnh Gia Lai cho biết đã đọc thông tin trên Báo Gia Lai. Thông tin khá mù mờ nhưng rất được người dân quan tâm, ông Hùng nói và cho biết hôm nay họp cả ngày nên chưa kịp yêu cầu Báo Gia Lai báo cáo. Trước đó, báo điện tử Gia Lai đã đăng tải bài báo Một công dân Gia Lai khẳng định phát hiện địa điểm máy bay MH370 rơi. Bài báo thông tin: 4 năm trước, người đàn ông này lúc ấy đang làm ăn tại Đắk Nông trong lúc tình cờ tìm kiếm thông tin hình ảnh vệ tinh trên mạng bỗng thấy một chiếc máy bay có kích thước giống chiếc máy bay MH370 rơi trong một lòng hồ. Sau đó, anh đã quay lại hình ảnh và vị trí chiếc máy bay này trên Google Earth. Hiện nay, lòng hồ mực nước dâng cao, không thể quan sát bằng mắt thường nếu đi trên mặt hồ hoặc chụp ảnh qua vệ tinh. Người này sau đó đã đưa clip lên YouTube, đến nay có hơn 5.700 lượt xem (Tuy nhiên, vì nhiều lý do nên đã được gỡ xuống) nhưng không ai ý kiến gì. Gần đây qua báo chí anh thấy một người Anh đưa thông tin đã phát hiện được máy bay MH370 tại rừng rậm Campuchia. Qua hình ảnh, anh nhận thấy clip của họ giống clip của anh nhưng có dấu hiệu chỉnh sửa hình ảnh máy bay trong clip mà anh đưa lên mạng cách đây 4 năm, vậy nên anh quyết định công bố thông tin này cho báo điện tử Gia Lai. Cũng theo báo điện tử Gia Lai, chiếc máy bay được người này phát hiện đo được độ dài khoảng 60,78m, sải cánh 31,23m, máy bay còn nguyên vẹn, không bị vỡ, đầu cắm xuống lòng hồ. Kích thước này tương đồng với thông tin về chiếc máy bay MH370 của Hãng Hàng không Malaysia. Chiếc máy bay này rơi xuống nước ở độ sâu khoảng 30m và nhiều khả năng ngập dưới bùn 5-6m, chứ không phải nằm trong rừng rậm và không thuộc địa phận Campuchia. Qua hình ảnh có thể thấy cánh chiếc máy bay méo mó, không nhìn rõ, chứng tỏ có thể trước khi rơi, máy bay va chạm nhẹ vào cây rừng hoặc bị ngập sâu dưới bùn đất. Anh này thậm chí còn khẳng định chỉ cần 2-3 ngày là tìm thấy chính xác vị trí chiếc máy bay MH370. Nếu Chính phủ Malaysia đồng ý anh sẽ xin phép các cơ quan chức năng thuê thợ lặn tìm kiếm. Việc tìm kiếm này nếu không đúng thì hãng hàng không Malaysia cũng không mất gì, toàn bộ chi phí người này sẽ chịu." * 16

import time


# target: 0.318 ms (16)
start = time.time()
ViTokenizer.tokenize(text)
end = time.time()
print(end - start)


# target: 2.55 s (16)
start = time.time()
x = word_tokenize(text)
end = time.time()
print(end - start)


