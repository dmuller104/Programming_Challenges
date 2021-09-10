#include <iostream>
#include <bits/stdc++.h>
using namespace std;

void display(const int arr[],const int len)
{
    for (int i=0;i<len;i++)
        cout << arr[i] << ", ";
    cout << endl;
}

void task(const int num_shoes)
{
    int count = 0;
    int shoes[2*num_shoes];
    for (int i=0;i<2*num_shoes;i++)
        shoes[i] = i/2 + 1;
    shuffle(shoes,shoes+2*num_shoes,default_random_engine());
    if (num_shoes < 50)
        display(shoes,num_shoes*2);
    int shoe_locs[num_shoes];
    for (int i=0;i<num_shoes;i++)
        shoe_locs[i] = -1;

    for (int i=0;i<2*num_shoes;i++)
    {
        if (shoe_locs[shoes[i]-1] == -1)
            shoe_locs[shoes[i]-1] = i;
        else if (shoe_locs[shoes[i]-1] / 2 == i/2)
            continue;
        else
        {
            const int static_pair_loc = shoe_locs[shoes[i]-1];
            const int static_pair = shoes[i];
            int moving_pair_loc = i;
            int moving_pair = shoes[i];
            int swap_shoe_loc = static_pair_loc + (static_pair_loc+1)%2 - static_pair_loc%2;
            int swap_shoe = shoes[swap_shoe_loc];
            if (num_shoes <= 20)
                cout << "Swapping index: " << moving_pair_loc << " " << swap_shoe_loc << endl;
            swap(shoes[moving_pair_loc],shoes[swap_shoe_loc]);
            count++;
            shoe_locs[swap_shoe-1] = moving_pair_loc;
            shoe_locs[moving_pair-1] = swap_shoe_loc;
        }
    }
    if (num_shoes < 50)
        display(shoes,num_shoes*2);
    cout << "Number of swaps: " << count << endl;
}

int main()
{
    int num_shoes;
    while (true)
    {
        cout << "\nNumber of shoes: ";
        cin >> num_shoes;
        task(num_shoes);
    }
    // crashes for num_shoes > 173019
    return 0;
}