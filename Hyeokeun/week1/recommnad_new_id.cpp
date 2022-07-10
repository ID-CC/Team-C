#include <string>
#include <vector>

using namespace std;

// 풀이에 걸린 시간 : 117분
string solution(string new_id) {
    string answer = "";
    
    answer = new_id;
	
	if (answer == "" || answer.empty() || answer.length() == 0) {
		answer = "a";
	}
	
	for (int i = answer.length() - 1; i >= 0; i--) {
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
			continue;
		}
	}

	if (answer.length() == 0) {
		answer = "a";
	}

	// step 3
	int cnt_dot = 0;
	int pos_dot = -1;
	for (int i = 0; i < answer.length(); i++) {
		if (answer.at(i) == '.') {
			cnt_dot++;
			if (pos_dot == -1) pos_dot = i;
		}
		else {
			if (cnt_dot > 1) {
				answer.erase(pos_dot + 1, cnt_dot - 1);
				i -= cnt_dot - 1;
			}
			cnt_dot = 0;
			pos_dot = -1;
		}
	}

	if (cnt_dot > 1) {
		answer.erase(pos_dot + 1, cnt_dot - 1);
	}

	// step 4
	if (answer.at(0) == '.') {
		answer.erase(0, 1);
	}

	// step 5
	if (answer.length() == 0) {
		answer = "a";
	}

	// step 4
	if (answer.at(answer.length() - 1) == '.') {
		answer.erase(answer.length() - 1, 1);
	}

	// step 6
	if (answer.length() >= 16) {
		answer.erase(15, answer.length() - 15);
		if (answer.at(answer.length() - 1) == '.') {
			answer.erase(answer.length() - 1, 1);
		}
	}

	// step 7
	if (answer.length() <= 2) {
		int redundance = 3 - answer.length();
		char ch = answer.at(answer.length() - 1);
		string last(1, ch);
		for (int i = 0; i < redundance; i++) {
			answer.append(last);
		}
	}
    
    return answer;
}