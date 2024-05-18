QFileDialog类的常用方法：

方法	说明
getOpenFileName()	获取一个打开文件的文件名
getOpenFileNames()	获取多个打开文件的文件名
getSaveFileName()	获取保存的文件名
getExistingDirectory()	获取一个打开的文件夹
setAcceptMode()	设置接收模式，取值如下。 QFileDialog.AcceptOpen:设置文件对话框为打开模式，这是默认值; OFileDialog.AcceptSave:设置文件对话框为保存模式
setDefaultSuffix()	设置文件对话框中的文件名的默认后缀名
setFileMode()	设置可以选择的文件类型，取值如下。 QFileDialog.FileMode.AnyFile:任意文件(无论文件是否存在）﹔ QFileDialog.FileMode.ExistingFile:已存在的文件; QFileDialog.FileMode.ExistingFiles:已存在的多个文件; QFileDialog.FileMode.Directory:文件夹; QFileDialog.FileMode.DirectoryOnly:文件夹（选择时只能选中文件夹)
setDirectory()	设置文件对话框的默认打开位置
setNameFilter()	设置名称过滤器，多个类型的过滤器之间用两个分号分割（例如:所有文件(.);Python文件(.py))﹔而一个过滤器中如果有多种格式，可以用空格分割(例如:图片文件(.jpg .png.bmp))
setViewMode()	设置显示模式，取值如下。 QFileDialog.Detail:显示文件详细信息，包括文件名、大小、日期等信息; QFileDialog.List:以列表形式显示文件名
selectedFile()	获取选择的一个文件或文件夹名字
selectedFiles()	获取选择的多个文件或文件夹名字



参考文章：

https://blog.csdn.net/potato123232/article/details/119103386

https://blog.csdn.net/caoli201314/article/details/135056556