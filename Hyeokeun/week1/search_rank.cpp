#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

// https://programmers.co.kr/learn/courses/30/lessons/72412
// 14:14 ~ 19:30 316분
// 정확도 100%, 효율성 2/4 통과

vector<string> split(string s, string divid) {
    vector<string> v;
    s += divid;
    int pos1 = 0, pos2 = -1;
    int cnt = 0;
    for (int i = 0; i < s.size(); i++) {
        if (divid.at(cnt) == s.at(i)) {
            if (cnt == 0) {
                pos2 = i - 1;
            }
            cnt++;
            if (cnt == divid.size()) {
                if (pos2 != -1)
                    v.push_back(s.substr(pos1, pos2 - pos1 + 1));

                pos1 = i + 1;
                pos2 = -1;
                cnt = 0;
            }
        }
        else if (cnt > 0) {
            pos2 = -1;
            cnt = 0;
        }
    }

    return v;
}

bool comp(int a, int b) {
    return a > b;
}

// 내림차순으로 정렬 된 list 내에서 target의 idx를 찾아 return
int binarySearch(vector<int> list, int target) {
    if (list.size() == 0) return 0;

    int left = 0;
    int right = list.size() - 1;
    int mid = 0;
    bool bSearch_sucess = false;
    while (right >= left) {
        mid = (left + right) / 2;

        if (list.at(mid) == target) {
            bSearch_sucess = true;
            break;
        }
        else if (list.at(mid) < target) {
            right = mid - 1;
        }
        else {
            left = mid + 1;
        }
    }

    // target을 찾지 못했을 때는 target보다 작은 값 중 가장 큰 값의 index (즉 target 이상의 값을 갖는 원소의 수)
    if (!bSearch_sucess) {
        if (list.at(mid) > target)
            return mid + 1;
        else
            return mid;
    }

    // target을 찾았으나, target과 같은 값을 갖는 원소가 여러 개일 경우 고려
    int search;
    while (mid < list.size()) {
        search = list.at(mid);
        if (search != target)
            break;
        mid++;
    }

    return mid;
}

class ApplicantTree {
public:    
    unordered_map<string, vector<int>> data;

    ApplicantTree() {
        data = unordered_map<string, vector<int>>();
    }

    void insert_data(vector<string> condition, int score, string cur = "", int depth = 0) {
        if (depth == condition.size()) {
            if (data.find(cur) == data.end()) {
                vector<int> vec = { score };
                data.insert(pair<string, vector<int>>(cur, vec));
            }
            else {
                vector<int>& vec = data.at(cur);
                vec.push_back(score);
            }
            return;
        }
        if (depth == 0) {
            insert_data(condition, score, condition.at(depth), depth + 1); // 명시 된 조건으로 검색할 때를 위함
            insert_data(condition, score, "-", depth + 1); // - 를 이용해서 검색할 때를 위함
        }
        else {
            insert_data(condition, score, cur + " and " + condition.at(depth), depth + 1); // 명시 된 조건으로 검색할 때를 위함
            insert_data(condition, score, cur + " and -", depth + 1); // - 를 이용해서 검색할 때를 위함
        }
    }

    int count_query(string query) {
        int pos = query.size() - 1;
        while (query.substr(pos, 1) != " ") {
            pos--;
        }
        string condition = query.substr(0, pos);
        int score = stoi(query.substr(pos + 1, query.size() - (pos + 1)));

        if (data.find(condition) == data.end()) 
            return 0;
        vector<int> vec = data.at(condition);
        int cnt = binarySearch(vec, score);
        return cnt;
    }
};

vector<int> solution(vector<string> info, vector<string> query) {
    vector<int> answer;

    ApplicantTree tree = ApplicantTree();

    vector<string> condition;
    vector<string> temp;
    int score;

    for (int i = 0; i < info.size(); i++) {
        condition = split(info.at(i), " ");
        score = stoi(condition.at(4));
        condition.erase(condition.begin() + 4);

        tree.insert_data(condition, score);
    }
    
    for (auto i = tree.data.begin(); i != tree.data.end(); i++) {
        vector<int>& vec = i->second;
        sort(vec.begin(), vec.end(), comp);
    }

    for (int i = 0; i < query.size(); i++) {
        string query_one = query.at(i);
        answer.push_back(tree.count_query(query_one));
    }

    return answer;
}