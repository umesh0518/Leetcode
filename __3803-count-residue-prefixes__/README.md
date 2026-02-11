# 3803. Count Residue Prefixes

You are given a string s consisting only of lowercase English letters.

A prefix of s is called a residue if the number of distinct characters in the prefix is equal to len(prefix) % 3.

Return the count of residue prefixes in s.
A prefix of a string is a non-empty substring that starts from the beginning of the string and extends to any point within it.
&nbsp;
Example 1:


Input: s = &quot;abc&quot;

Output: 2

Explanation:​​​​​​​


	Prefix &quot;a&quot; has 1 distinct character and length modulo 3 is 1, so it is a residue.
	Prefix &quot;ab&quot; has 2 distinct characters and length modulo 3 is 2, so it is a residue.
	Prefix &quot;abc&quot; does not satisfy the condition. Thus, the answer is 2.



Example 2:


Input: s = &quot;dd&quot;

Output: 1

Explanation:


	Prefix &quot;d&quot; has 1 distinct character and length modulo 3 is 1, so it is a residue.
	Prefix &quot;dd&quot; has 1 distinct character but length modulo 3 is 2, so it is not a residue. Thus, the answer is 1.



Example 3:


Input: s = &quot;bob&quot;

Output: 2

Explanation:


	Prefix &quot;b&quot; has 1 distinct character and length modulo 3 is 1, so it is a residue.
	Prefix &quot;bo&quot; has 2 distinct characters and length mod 3 is 2, so it is a residue. Thus, the answer is 2.



&nbsp;
Constraints:


	1 &lt;= s.length &lt;= 100
	s contains only lowercase English letters.

