#ローマ字を整数で返すプログラム
class Solution:
    # str で受け取り int で返す
    def romanToInt(self, s: str) -> int:
        # ローマ数字の記号と値の対応を辞書に保存
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        # 変換する前の合計を初期化
        result = 0

        # 左から右に捜査し、前の値と比較して加算、減算する
        for i in range(len(s)):
            if i > 0 and roman_dict[s[i]] > roman_dict[s[i-1]]:
                result += roman_dict[s[i]] - 2 * roman_dict[s[i-1]] # 減算する場合

            else:
                result += roman_dict[s[i]]

        return result