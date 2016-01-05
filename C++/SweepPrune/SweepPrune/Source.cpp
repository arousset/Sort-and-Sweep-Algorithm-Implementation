#include "vectors.h"

void main()
{
	Rect a(15, 50, { 50, 50 }, 'a');
	Rect b(15, 100, { 40, 70 }, 'b');
	Rect c(15, 150, { 60, 30 }, 'c');

	Node min1(a, min, true, 1);
	Node max1(a, max, false, 1);
	Node min2(b, min, true, 2);
	Node max2(b, max, false, 2);
	Node min3(c, min, true, 3);
	Node max3(c, max, false, 3);

	min1.SetNext(max1);
	max1.SetNext(min2);
	min2.SetNext(max2);
	max2.SetNext(min3);
	min3.SetNext(max3);

	Node *current = &min1;

	for (int i = 0; i <= 50; i++)
	{
		if (current->next != NULL)
		{
			Node *Compare = current->next;
			if (current->Compare(*Compare) == false)
			{
				Compare->Remove();
				Compare->Insert(current->pre, current);
				Node *change = current->next;
				current = change;
			}
			else if (min1.sortCompare(min1) == false)
			{
				current = &min1;
			}
			else
			{
				break;
			}
		}
	}

	system("pause");
}