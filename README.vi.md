# Xây dựng model tách từ trong xử lí văn bản tiếng Việt

## Cấu trúc

```
word_tokenize/
  ├─ data/                                  <!-- chứa dữ liệu trong quá trình huấn luyện và đánh giá mô hình 
  |   └─── vlsp2016/                        <!-- dữ liệu từ vlsp 2016
  |         ├── corpus/   
  |         │   ├── dev.txt                 <!-- dữ liệu đánh giá trong quá trình huấn luyện
  |         │   ├── test.txt                <!-- dữ liệu đánh giá mô hình
  |         │   └── train.txt               <!-- dữ liệu huấn luyện
  |         ├── raw/                        <!-- dữ liệu thô
  |         │   ├── dev.txt
  |         │   ├── test.txt
  |         │   └── train.tx
  |         └── preprocess.py               <!-- các bước tiền xử lí dữ liệu thô đưa vào corpus
  └─ experiments/                           <!-- chứa các thí nghiệm với feature và model.
      ├── crf/                              <!-- thử nghiệm mô hình với CRF
      |     ├── exported/                   <!-- kết quả thử nghiệm
      |     │   ├── reports.txt
      |     ├── model/                      
      |     │   ├── __init__.py             <!-- hàm tách từ
      |     │   ├── model.bin
      |     │   └── transformer.bin
      |     ├── analyze.py                  <!-- đánh giá mô hình với dữ liệu test 
      |     ├── custom_transformer.py       <!-- các bước biến đổi dữ liệu
      |     ├── load_data.py                <!-- lấy dữ liệu từ corpus
      |     ├── model.py                    <!-- các quá trình huấn luyện dữ liệu
      |     ├── punctuation.txt                
      |     ├── score.py                    <!-- kết quả f1 của mô hình
      |     ├── test_model.py               <!-- các thí nghiệm nhỏ kiểm tra hoạt động của mô hình
      |     ├── train.py                    <!-- các bước thực hiện huấn luyện
      |     └── to_column.py                <!-- biến dữ liệu dạng câu thành dạng CoNLL
      └── crf_techbk/
            ├── feature_engineering/        <!-- các tính năng cho mô hình
            |   ├── __init__.py
            │   ├── crfutils.py
            │   ├── features.py
            │   └── word_pattern.py
            ├── model/                      <!-- chứa mô hình sau khi huấn luyện
            │   └── model.bin
            ├── tools/ 
            │   ├── __init__.py
            │   ├── readers.py              <!-- đọc dữ liệu
            │   └── writers.bin             <!-- định dạng dữ liệu
            ├── load_data.py                <!-- lấy dữ liệu từ corpus
            ├── model.py                    <!-- huấn luyện dữ liệu
            ├── predict.py                  <!-- tách từ, sử dụng mô hình đã huấn luyện
            ├── process.py                  <!-- trích rút đặc trưng
            ├── reports.txt                 <!-- kết quả đánh giá mô hình
            ├── text.py                     
            └── words.py                    <!-- từ điển tiếng Việt
```
## Xây dựng mô hình

**Bước 1**: Chuẩn bị dữ liệu  

Dữ liệu trước xử lí đặt tại thư mục raw gồm các file text: `train.txt`, `dev.txt`, `test.txt`. Quá trình tiền xử lí bao gồm các bước: lấy token tại cột đầu tiên của dữ liệu raw, biến đổi từng token với mỗi token đơn thành `B-W`, với những token gồm word và dấu `_` thì word đầu tiên là `B-W`, các word sau là `I-W`. 

Dữ liệu sau khi xử lí sẽ được đưa vào các file tương ứng trong `corpus`.

**Bước 2**: Huấn luyện dữ liệu

Lấy dữ liệu từ corpus bằng hàm `load_data`. 

Sau đó biến đổi dữ liệu bằng hàm `custom_transformer` với các temple lấy từ file `feature_template.py`. Chia dữ liệu thành 2 phần train và test bằng hàm `train_test_split` với `test_size=0.1`. 

Sử dụng CRF để huấn luyện dữ liệu `train` đã được chia từ bước trên. Mô hình và các biến đổi dữ liệu được đóng gói lần lượt thành file `model.bin`, `transfomer.bin` và lưu tại thư mục model.

**Bước 3**: Đánh giá mô hình

Từ mô hình đã huấn luyện, tiến hành dự đoán với dữ liệu `test`. So sánh dữ liệu dự đoán và dữ liệu đánh giá để tính chỉ số `F1`.

