# Xây dựng model tách từ trong xử lí văn bản tiếng Việt

## Cấu trúc
| Thư mục                                                                                                                                                                                                           | Mục đích                                                                                                                                                                                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| data                                                                                                                                                                                                              | Chứa dữ liệu trong quá trình huấn luyện                                                                                                                                                                                                                   |
|  anonymous<br/>&nbsp;&nbsp;&nbsp; corpus<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; train<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; test<br/>&nbsp;&nbsp;&nbsp;&nbsp; raw<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; input<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; output<br/>&nbsp;&nbsp;&nbsp; eda<br/>&nbsp;&nbsp;&nbsp; preprocess.py<br/>&nbsp;&nbsp;&nbsp; eda.py<br/>                                                                                     | Với dữ liệu thu thập được tiến hành phân vào các thư mục  - raw: chứa dữ liệu thô - corpus: chứa dữ liệu cho việc huấn luyện và đánh giá mô hình. Các file preprocess.py và eda.py giúp phân loại và đánh giá sơ bộ dữ liệu trên.                         |
|  vlsp2016<br/>&nbsp;&nbsp;&nbsp; corpus<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; train.txt<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; test.txt<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; dev.txt<br/>&nbsp;&nbsp;&nbsp; raw<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; train.txt<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; test.txt<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; dev.txt<br/>&nbsp;&nbsp;&nbsp; preprocess.py                                                                              | Dữ liệu từ vlsp 2016 định dạng CoNLL đã phân làm các file train, test, dev tương ứng  được lưu tại thư mục rawFile preprocess.py biến đổi dữ liệu trên về các file tương ứng với định dạng: ``` Chúng BW ta IW thường BW nói BW đến BW Rau BW sạch IW ``` |
| experiments                                                                                                                                                                                                       | chứa các thử nghiệm và đánh giá mô hình với các feature và model.                                                                                                                                                                                         |
| crf<br/>&nbsp;&nbsp;&nbsp; models<br/>&nbsp;&nbsp;&nbsp; load_data.py<br/>&nbsp;&nbsp;&nbsp; score.py<br/>&nbsp;&nbsp;&nbsp; train.py<br/>&nbsp;&nbsp;&nbsp;&nbsp;custom_transformer.py<br/>&nbsp;&nbsp;&nbsp;&nbsp;feature_template.py                                                                                                          | Thử nghiệm model crf tại file train.py sử dụng các feature tại feature_temple.py và các biến đổi từ custom_transformer.py trên dữ liệu vlsp2016 được lấy từ load_data.py. File score.py giúp đưa ra các đánh giá dựa trên tỉ số F1.                       |
| crf_techbk<br/>&nbsp;&nbsp;&nbsp; feature_engineering<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; crfutils.py<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; features.py<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; word_pattern.py<br/>&nbsp;&nbsp;&nbsp; models<br/>&nbsp;&nbsp;&nbsp; tools<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; readers.py<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; writers.py<br/>&nbsp;&nbsp;&nbsp; load_data.py<br/>&nbsp;&nbsp;&nbsp; model.py<br/>&nbsp;&nbsp;&nbsp; predict.py<br/>&nbsp;&nbsp;&nbsp; process.py<br/>&nbsp;&nbsp;&nbsp; text.py<br/>&nbsp;&nbsp;&nbsp; words.txt              |Thử nghiệm model crf tại file model.py sử dụng các feature tại thư mục feature_engineering và các biến đổi từ preprocess.py trên dữ liệu vlsp2016 được lấy từ load_data.py, đồng thời đưa ra các đánh giá dựa trên tỉ số F1.

## Xây dựng mô hình

<strong>Bước 1</strong>: Tiền xử lí dữ liệu (dữ liệu vlsp2016). 

Dữ liệu trước xử lí đặt tại thư mục raw gồm các file text: train, dev, test. Quá trình tiền xử lí bao gồm các bước: lấy token tại cột đầu tiên của dữ liệu raw, biến đổi từng token với mỗi token đơn thành "BW", với những token gồm word và dấu "_" thì word đầu tiên là "BW", các word sau là "IW". 

Dữ liệu sau khi xử lí sẽ được đưa vào các file tương ứng trong corpus.

<strong>Bước 2</strong>: Huấn luyện dữ liệu

Lấy dữ liệu từ corpus bằng hàm load_data. 

Sau đó biến đổi dữ liệu bằng hàm custom_transformer với các temple lấy từ file feature_template.py. Chia dữ liệu thành 2 phần train và test bằng hàm train_test_split với test_size=0.1. 

Sử dụng CRF để huấn luyện dữ liệu train đã được chia. Mô hình được đóng gói thành file model.bin và lưu tại thư mục models.

<strong>Bước 3</strong>: Đánh giá mô hình
Từ mô hình đã huấn luyện, tiến hành dự đoán với dữ liệu test. So sánh dữ liệu dự đoán và dữ liệu đánh giá để tính chỉ số F1.

