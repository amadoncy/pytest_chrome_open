"""
1.要选所有的option元素 和所有的 h4 元素，可以使用    //option | //h4
                            等同于CSS选择器     option , h4
                                             //*[@class='single_choice'] | //*[@class='multi_choice']
                            等同于CSS选择器    .single_choice , .multi_choice

2.要选择 id 为 china 的节点的父节点，可以这样写 //*[@id='china']/..
                                        /..  这个可以表示为寻找当前标签的父节点  /../..还可以继续往上找
                                        

3.比如，要选择 class 为 single_choice 的元素的所有后续兄弟节点 //*[@class='single_choice']/following-sibling::*
4.如果，要选择后续节点中的div节点， 就应该这样写 //*[@class='single_choice']/following-sibling::div
xpath还可以选择 前面的 兄弟节点，用这样的语法 preceding-sibling::
5.要选择 class 为 single_choice 的元素的 所有 前面的兄弟节点，这样写  //*[@class='single_choice']/preceding-sibling::*
6.要选择 class 为 single_choice 的元素的  前面最靠近的兄弟节点 , 这样写   //*[@class='single_choice']/preceding-sibling::*[1]
7.前面第2靠近的兄弟节点 , 这样写    //*[@class='single_choice']/preceding-sibling::*[2]



8.
要在某个元素内部使用xpath选择元素， 需要 在xpath表达式最前面加个点 .
像这样    elements = china.find_elements(By.XPATH, './/p')
"""