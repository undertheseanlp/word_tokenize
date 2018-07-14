from unittest import TestCase
from final_model import word_tokenize


class TestWordSent(TestCase):
    def test_word_tokenize_1(self):
        text = "Vẫn trăn trở việc phá dỡ công trình xâm hại di sản Tràng An"
        actual = word_tokenize(text, format="text")
        expected = 'Vẫn trăn_trở việc phá dỡ công_trình xâm_hại di_sản Tràng_An'
        self.assertEquals(actual, expected)

    def test_word_tokenize_2(self):
        text = "Người đàn ông nhịn đói đi bộ suốt 6 ngày để trốn khỏi trại vàng"
        actual = word_tokenize(text, format="text")
        expected = 'Người đàn_ông nhịn_đói đi_bộ suốt 6 ngày để trốn khỏi trại vàng'
        self.assertEquals(actual, expected)

    def test_word_tokenize_3(self):
        text = "Nông dân Hà Nội tất bật thu hoạch dâu chín"
        actual = word_tokenize(text, format="text")
        expected = 'Nông_dân Hà_Nội tất_bật thu_hoạch dâu chín'
        self.assertEqual(actual, expected)

    def test_word_tokenize_4(self):
        text = "Nghi vấn mới về hung thủ hạ độc cựu điệp viên hai mang Nga"
        actual = word_tokenize(text, format="text")
        expected = 'Nghi_vấn mới về hung_thủ hạ độc cựu điệp_viên hai mang Nga'
        self.assertEqual(actual, expected)
