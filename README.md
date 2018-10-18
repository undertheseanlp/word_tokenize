# Tách từ tiếng Việt

![](https://img.shields.io/badge/made%20with-%E2%9D%A4-red.svg)
![](https://img.shields.io/badge/opensource-vietnamese-blue.svg)
![](https://img.shields.io/badge/build-passing-green.svg)


Dự án nghiên cứu về bài toán tách từ tiếng Việt, được phát triển bởi nhóm nghiên cứu xử lý ngôn ngữ tự nhiên tiếng Việt - [underthesea](https://github.com/undertheseanlp). Chứa mã nguồn các thử nghiệm cho việc xử lý dữ liệu, huấn luyện và đánh giá mô hình, cũng như cho phép dễ dàng tùy chỉnh mô hình đối với những tập dữ liệu mới.

**Nhóm tác giả** 

* Vũ Anh ([anhv.ict91@gmail.com](anhv.ict91@gmail.com))
* Bùi Nhật Anh ([buinhatanh1208@gmail.com](buinhatanh1208@gmail.com))
* Đoàn Việt Dũng ([doanvietdung273@gmail.com](doanvietdung273@gmail.com))

**Tham gia đóng góp**

Mọi ý kiến đóng góp hoặc yêu cầu trợ giúp xin gửi vào mục [Issues](../../issues) của dự án. Các thảo luận được khuyến khích **sử dụng tiếng Việt** để dễ dàng trong quá trình trao đổi. 

Nếu bạn có kinh nghiệm trong bài toán này, muốn tham gia vào nhóm phát triển với vai trò là [Developer](https://github.com/undertheseanlp/underthesea/wiki/H%C6%B0%E1%BB%9Bng-d%E1%BA%ABn-%C4%91%C3%B3ng-g%C3%B3p#developercontributor), xin hãy đọc kỹ [Hướng dẫn tham gia đóng góp](https://github.com/undertheseanlp/underthesea/wiki/H%C6%B0%E1%BB%9Bng-d%E1%BA%ABn-%C4%91%C3%B3ng-g%C3%B3p#developercontributor).

## Mục lục

* [Yêu cầu hệ thống](#yêu-cầu-hệ-thống)
* [Thiết lập môi trường](#thiết-lập-môi-trường)
* [Hướng dẫn sử dụng](#hướng-dẫn-sử-dụng)
  * [Sử dụng mô hình đã huấn luyện sẵn](#sử-dụng-mô-hình-đã-huấn-luyện-sẵn)
  * [Huấn luyện mô hình](#huấn-luyện-mô-hình) 
* [Trích dẫn](#trích-dẫn)
* [Bản quyền](#bản-quyền)

## Yêu cầu hệ thống 

* `Hệ điều hành: Linux (Ubuntu, CentOS), Mac`
* `Python 3.6`
* `Anaconda`
* `languageflow==1.1.7`

## Thiết lập môi trường

Tải project bằng cách sử dụng lệnh `git clone`

```
$ git clone https://github.com/undertheseanlp/classification.git
```

Tạo môi trường mới và cài đặt các gói liên quan

```
$ cd word_tokenize
$ conda create -n word_tokenize python=3.6
$ pip install -r requirements.txt
```

## Hướng dẫn sử dụng

Trước khi chạy các thử nghiệm, hãy chắc chắn bạn đã activate môi trường `word_tokenize`, mọi câu lệnh đều được chạy trong thư mục gốc của dự án.

```
$ cd word_tokenize
$ source activate word_tokenize
``` 

### Sử dụng mô hình đã huấn luyện sẵn

```
$ python word_tokenize.py --text "Chàng trai 9X Quảng Trị khởi nghiệp từ nấm sò"
$ python word_tokenize.py --fin tmp/input.txt --fout tmp/output.txt
```

### Huấn luyện mô hình

**Huấn luyện mô hình mới**

```
$ python util/preprocess_vlsp2013.py
$ python train.py \
    --train tmp/vlsp2013/train.txt \
    --model tmp/model.bin
```

**Kiểm tra mô hình vừa huấn luyện**

```
$ python word_tokenize.py \
    --fin tmp/input.txt --fout tmp/output.txt \
    --model tmp/model.bin
```

## Trích dẫn

Nếu bạn thấy mã nguồn này hữu ích, xin hãy trích dẫn đường dẫn của dự án trong các nghiên cứu của mình 

```
@online{undertheseanlp/word_tokenize,
author ={Vu Anh, Bui Nhat Anh, Doan Viet Dung},
year = {2018},
title ={Xây dựng hệ thống tách từ tiếng Việt của nhóm underthesea},
url ={https://github.com/undertheseanlp/word_tokenize}
}
```

## Bản quyền

Mã nguồn của dự án được phân phối theo giấy phép [GPL-3.0](LICENSE.txt).