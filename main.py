#take file as input.
# read as text

#variable resourceDict
# scan through every char / word.
#identify < save position/index of it
#if has a "# combo, then assume its a color
#set flag to indicate color found
# get the whole expression all the way to end of "
# save position of the first "#
#continue
#identify > save position /  index of it  IF flag true. otherwise continue

#if flag true:
#go to the index position of the first "#
#save color content inside " "
#check if color inside resources dictionary (resourceDict)
#if it is, check resource name for that color
#set name = that name
#if not:
#within <>, search for Name="
#extract name by saving content inside " "
#check if name exists in the resource dictionary
#if so continue adding a number till not found / name doesnt exist
#set name = that

# replace text in "" with {StaticResource name}

#go back to line 4 / continue scanning / iterating


#when finished, check resourceDict
#create .xaml based on the rsource dictionary
