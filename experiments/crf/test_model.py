from unittest import TestCase
from model import word_sent


class TestWordSent(TestCase):
    def test_word_sent_1(self):
        text = "Thủ tướng quyết định mở rộng Sân bay Tân Sơn Nhất về phía Nam"
        actual = word_sent(text, format="text")
        expected = 'Thủ_tướng quyết_định mở_rộng Sân_bay Tân_Sơn_Nhất về phía Nam'
        self.assertEquals(actual, expected)

    def test_word_sent_2(self):
        text = "HLV Park Hang Seo thực hiện một thử nghiệm khá thành công ở trận đấu giữa đội tuyển Việt Nam và Jordan"
        actual = word_sent(text, format="text")
        expected = 'HLV Park_Hang_Seo thực_hiện một thử_nghiệm khá thành_công ở trận đấu giữa đội_tuyển Việt_Nam và Jordan'
        self.assertEquals(actual, expected)

    def test_word_sent_3(self):
        text = "Chúng ta thường nói đến Rau sạch, Rau an toàn để phân biệt với các rau bình thường bán ngoài chợ."
        actual = word_sent(text, format="text")
        expected = 'Chúng_ta thường nói đến Rau sạch, Rau an_toàn để phân_biệt với các rau bình_thường bán ngoài chợ.'
        self.assertEqual(actual, expected)
