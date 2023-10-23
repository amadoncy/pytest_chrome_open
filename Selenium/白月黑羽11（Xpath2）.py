'''
根据属性名来查找元素  [@属性名='属性值']

比如选择 具有multiple属性的所有页面元素 ，可以这样 //*[@multiple]

属性值包含字符串
要选择 style属性值 包含 color 字符串的 页面元素 ，可以这样 //*[contains(@style,'color')]

要选择 style属性值 以 color 字符串 开头 的 页面元素 ，可以这样 //*[starts-with(@style,'color')]

要选择 style属性值 以 某个 字符串 结尾 的 页面元素 ，大家可以推测是 //*[ends-with(@style,'color')]



'''