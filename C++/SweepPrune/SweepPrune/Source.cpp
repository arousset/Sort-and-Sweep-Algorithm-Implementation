#include "vectors.h"

int main()
{
	Rect rec1(25, 100, { 50, 50 }, 'a');		
	Rect rec2(50, 200, { 75, 150 }, 'b');
	Rect rec3(25, 50, { 200, 50 }, 'c');

	Node min1(rec1.min, true, 1);	//Min and Maxes for rectangles
	Node max1(rec1.max, false, 1);

	Node min2(rec2.min, true, 2);
	Node max2(rec2.max, false, 2);

	Node min3(rec3.min, true, 3);
	Node max3(rec3.max, false, 3);

	min1.SetNext(max1);	//Putting in a linked list
	max1.SetNext(min2);
	min2.SetNext(max2);
	max2.SetNext(min3);
	min3.SetNext(max3);

	Node *current = &min1;	//Acess to list

	for (int s = 0; s <= 50; s++)//sorts list from least to greatest
	{
		if (current == NULL)
		{
			break;
		}

		if (current->next != NULL)//Not at end
		{
			Node *compare = current->next;				//Grabbing current's next for comparison
			if (current->Compare(*compare) == false)	//Compares the current value to the next's value
			{
				compare->Remove();						//Removes comparison and changes order
				compare->Insert(current->pre, current);	//Compare gets put before current.
			}
		}

		else if (min1.SortCompare(min1) == false)		//Checks list to see if from least to greatest
		{
			current = &min1;							//if not in order, Restart from beginning
		}

		else if (min1.SortCompare(min1) == true)			
		{
			break;
		}

		Node *change = current->next;					//Current is now the next
		current = change;
	}

	min1.read(min1);//Reads rearranged list.

					
	Vector<int> active[10];	//Active list



	for (int r = 0; r < 10; r++)	//Print out active list
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