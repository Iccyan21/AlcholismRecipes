# 個別の整数のソートされた配列とターゲット値を指定すると、
# ターゲットが見つかった場合はインデックスを返します。
# そうでない場合は、順番に挿入された場合のインデックスを返します。

List = [1,3,5,6]

target = 5

class Solution:
    # Listのint型とtargetのint型を受け取りintで返す。
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = right -1

        return left
