"""

1.要选择 p类型第2个的子元素，就是  //p[2]
2.要选取父元素为div 中的 p类型 第2个 子元素  //div/p[2]
3.选择父元素为div的第2个子元素，不管是什么类型 //div/*[2]
4.
选取p类型倒数第1个子元素   //p[last()]
选取p类型倒数第2个子元素  //p[last()-1]

5.范围选择
例如 ：
    上层元素为class属性下面的 1-2个子元素
      //*[@class='multi_choice']/*[position()<=3]

    选取option类型第1到2个子元素
     //option[position()<=2]
"""