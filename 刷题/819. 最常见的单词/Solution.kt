
/**
 * 给定一个段落 (paragraph) 和一个禁用单词列表 (banned)。返回出现次数最多，同时不在禁用列表中的单词。
 * 题目保证至少有一个词不在禁用列表中，而且答案唯一。
 * 禁用列表中的单词用小写字母表示，不含标点符号。段落中的单词不区分大小写。答案都是小写字母。
 */
class Solution {
    fun mostCommonWord(paragraph: String, banned: Array<String>): String {
        // 先都转为小写
        paragraph.toLowCase()
    }
}

fun main() {
    val paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    val banned = ["hit"]
}