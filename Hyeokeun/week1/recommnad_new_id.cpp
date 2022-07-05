#include <string>
#include <vector>

using namespace std;

string solution(string new_id) {
    string answer = "";
    
    answer = new_id;
	int len_id = answer.length();

	if (answer == "" || answer.empty() || answer.length() == 0) {
		answer = "a";
		len_id = 1;
	}
	
	for (int i = len_id - 1; i >= 0; i--) {
		char this_char = answer.at(i);
		// step 1
		if (this_char >= 'A' && this_char <= 'Z') {
			this_char += 32;
			string replace_str(1, this_char);
			answer.replace(i, 1, replace_str);
		}
		// step 2
		if ( (this_char < 'a' || this_char > 'z') && (this_char < '0' || this_char > '9') && this_char != '-' && this_char != '_' && this_char != '.') {
			answer.erase(i, 1);
			len_id--;
			continue;
		}
	}

	if (len_id == 0) {
		answer = "a";
		len_id = 1;
	}

	// step 3
	int cnt_dot = 0;
	int pos_dot = -1;
	for (int i = 0; i < len_id; i++) {
		if (answer.at(i) == '.') {
			cnt_dot++;
			if (pos_dot == -1) pos_dot = i;
		}
		else {
			if (cnt_dot > 1) {
				answer.erase(pos_dot + 1, cnt_dot - 1);
				len_id -= cnt_dot - 1;
				i -= cnt_dot - 1;
			}
			cnt_dot = 0;
			pos_dot = -1;
		}
	}

	if (cnt_dot > 1) {
		answer.erase(pos_dot + 1, cnt_dot - 1);
		len_id -= cnt_dot - 1;
	}

	if (len_id == 0) {
		answer = "a";
		len_id = 1;
	}

	// step 4
	if (answer.at(0) == '.') {
		answer.erase(0, 1);
		len_id--;
	}

	// step 5
	if (len_id == 0) {
		answer = "a";
		len_id = 1;
	}

	// step 4
	if (answer.at(len_id - 1) == '.') {
		answer.erase(len_id - 1, 1);
		len_id--;
	}

	// step 6
	if (len_id >= 16) {
		answer.erase(15, len_id - 15);
		len_id = 15;
		if (answer.at(len_id - 1) == '.') {
			answer.erase(len_id - 1, 1);
			len_id--;
		}
	}

	// step 7
	if (len_id <= 2) {
		int redundance = 3 - len_id;
		char ch = answer.at(len_id - 1);
		string last(1, ch);
		for (int i = 0; i < redundance; i++) {
			answer.append(last);
		}
	}
    
    return answer;
}