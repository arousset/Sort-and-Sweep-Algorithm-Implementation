#include "vectors.h"

int main()
{
	Rect rec1(25, 100, { 50, 50 }, 'a');
	Rect rec2(50, 200, { 75, 150 }, 'b');
	Rect rec3(25, 50, { 200, 50 }, 'c');

	Node min1(rec1.min, true, 1);
	Node max1(rec1.max, false, 1);

	Node min2(rec2.min, true, 2);
	Node max2(rec2.max, false, 2);

	Node min3(rec3.min, true, 3);
	Node max3(rec3.max, false, 3);

	min1.SetNext(max1);
	max1.SetNext(min2);
	min2.SetNext(max2);
	max2.SetNext(min3);
	min3.SetNext(max3);

	Node *current = &min1;

	for (int s = 0; s <= 50; s++)
	{
		if (current == NULL)
		{
			break;
		}

		if (current->next != NULL)
		{
			Node *compare = current->next;
			if (current->Compare(*compare) == false)
			{
				compare->Remove();
				compare->Insert(current->pre, current);
			}
		}

		else if (min1.SortCompare(min1) == false)
		{
			current = &min1;
		}

		else if (min1.SortCompare(min1) == true)
		{
			break;
		}

		Node *change = current->next;
		current = change;
	}

	Vector<int> active[10];	

	current = &min1;
	int nump = 1;
	int *num = &nump;
	int arr = 0;
	Node *start = NULL;	
	Node *end = NULL;	

	for (int sor = 0; sor < 500; sor++)
	{
		if (num >= 4)
		{
			break;
		}

		if (current == end)
		{
			end = NULL;
			start = NULL;
			current = &min1;
			*num += 1;
		}

		if (current != NULL || current != end)
		{
			if (current->belong == *num && current->minMax == true)
			{
				start = current;
			}

			else if (current->belong == *num && current->minMax == false)
			{
				end = current;
			}
		}

		if (start != NULL && end != NULL)
		{
			current = start->next;
			active[arr] = current->CompareName(*num);	
			arr += 1;								
		}

		current = current->next;	
	}

	for (int r = 0; r < arr; r++)	
	{
		if (active[r].x > 0 || active[r].y > 0)
		{
			if (active[r - 1].x + active[r].x != active[r - 1].y + active[r].y)
			{
				cout << active[0 + r].x << ", " << active[r].y << endl;
			}
		}
	}

	system("pause");
}