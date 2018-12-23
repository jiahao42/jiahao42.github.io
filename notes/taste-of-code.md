---
layout: term
title: Taste of code
pwd: notes/taste-of-code
cmd: cat taste-of-code
---

<img src="./imgs/linus-on-TED.png" alt="Linus on TED" height="250"/>

今天在YouTube上看了[Linus Torvalds的一场TED](https://www.youtube.com/watch?v=o8NPllzkFhE)，Linus拿了一小段代码来说明代码的taste问题。

代码很简单，就是在一个单向链表里删除一个指定结点，一般学校里教的写法都是像下面这样的：

```C
void remove_list_entry(linked_list* entry) {
    linked_list* prev = NULL;
    linked_list* walk = head;

    //Walk the list 

    while (walk != entry) {
        prev = walk;
        walk = walk->next;
    }

    // Remove the entry by updating the
    // head or the previous entry
    
    if (!prev) {
        head = entry->next;
    } else {
        prev->next = entry->next;
    }
}
```

值得注意的是，在代码的结尾有一个if statement，这是用来区分两种情况的：

* 被删除的结点是这个单向链表的头结点，此时我们需要一个新的头结点，
* 被删除的结点不是这个单向链表的第一个结点，此时我们只需将被删除结点的前置结点的next指针指向被删除结点的后置结点即可。

但是Linus认为这种写法是没有taste的，他更喜欢下面的这种写法：

```C
void remove_list_entry(linked_list* entry) {
    // The "indirect" pointer points to the
    // *address* of the thing we'll update

    linked_list** indirect = &head;

    // Walk the list, looking for the thing that
    // points to the entry we want to remove

    while ((*indirect) != entry)
        indirect = &(*indirect)->next;
        
    // .. and just remove it
    *indirect = entry->next;
}
```

与上面的写法不同，这里我们直接将需要被删除结点的后置结点的next地址复制到被删除结点的前置结点的next指针上，无需考虑被删除结点是否是头结点这个问题，从而也省去了第一段代码中的if statement，这毫无疑问是更加方便的做法。

下面说一下第二段代码的原理。

首先下面的是我们这里用到的`linked_list`的定义，普通的链表结点：

```C
typedef struct Node {
    int data;
    struct Node *next;
} linked_list;
```

假设此时我们的链表中有5个结点，其内容分别是1/2/3/4/5，有一`head`指针指向头结点，我们希望删除结点2。

```text
                          entry -+
   head                          |
      +---+     +-------+     +-------+     +-------+     +-------+     +--------+
      |   |---->| 1 |   |---->| 2 |   |---->| 3 |   |---->| 4 |   |---->| 5 |NULL|
      +---+     +-------+     +-------+     +-------+     +-------+     +--------+
```

`linked_list** indirect = &head;`这一行代码将会构造一个指向`head`指针的二级指针：

```text
                         entry -+
  head                          |
     +---+     +-------+     +-------+     +-------+     +-------+     +--------+
     |   |---->| 1 |   |---->| 2 |   |---->| 3 |   |---->| 4 |   |---->| 5 |NULL|
     +---+     +-------+     +-------+     +-------+     +-------+     +--------+
       ^
       |
     +---+
     |   |
     +---+
   indirect
```


接下来是一个`while loop`

```C
while ((*indirect) != entry)
  indirect = &(*indirect)->next;
```

首先一开始`indirect`指向`head`，而`*indirect`则等于head指针再被evaluate一次，那么就是指向了链表的头结点，很显然此时的`*indirect`不等于`entry`，因为entry指向的是第二个结点。于是进入`while loop`执行`indirect = &(*indirect)->next;`，因为`*indirect`指向头结点，那么`&(*indirect)->next`就可以取得*头结点的next指针所在的地址*，这一行就相当于将头结点的next指针的地址赋给了`indirect`，那么`*indirect`就相当于evaluate了头结点中next指针中所存储的地址，也就是第二个结点，也就是entry。此时再判断，发现`(*indirect) == entry`，退出该`while loop`。

最后执行`*indirect = entry->next;`，由于`indirect`指向头结点的next指针的地址而`*indirect`则等效与头结点的next指针，所以实际上这行代码就是将头结点的next指针指向entry的下一个元素，从而完美地将entry从链表中删去。

```text
                          entry -+
   head                          |
      +---+     +-------+     +-------+     +-------+     +-------+     +--------+
      |   |---->| 1 |   |--   | 2 |   |---->| 3 |   |---->| 4 |   |---->| 5 |NULL|
      +---+     +-------+  \  +-------+     +-------+     +-------+     +--------+
                  *indirect \              /
                             +------------+
```                             

---

Thanks to the discussion on the Internet:   

* 1) [Using pointers to remove item from singly-linked list](https://stackoverflow.com/questions/12914917/using-pointers-to-remove-item-from-singly-linked-list)
* 2) [delete an entry from a singly-linked list](https://stackoverflow.com/questions/51794426/delete-an-entry-from-a-singly-linked-list/51796733#51796733)
* 3) [Applying the Linus Torvalds “Good Taste” Coding Requirement](https://news.ycombinator.com/item?id=12793624)


(The End)