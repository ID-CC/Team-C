#include <string>
#include <vector>

#define INFO_LEN 5

using namespace std;

// 203분 소요
vector<string> split(string s, string divid) {
    vector<string> v;
    s += divid;
    int pos1 = 0, pos2 = -1;
    int itr = 0;
    int cnt = 0;
    for (int i = 0; i < s.size(); i++) {
        if (divid.at(cnt) == s.at(i)) {
            if (cnt == 0) {
                pos2 = i - 1;
            }
            cnt++;
        }

        if (cnt == divid.size()) {
            if (pos2 != -1)
                v.push_back(s.substr(pos1, pos2 - pos1 + 1));

            pos1 = i + 1;
            pos2 = -1;
            cnt = 0;
        }
    }

    return v;
}

class Info {
public:
    string m_language;
    string m_major;
    string m_career;
    string m_favour;
    int m_score;

public:
    Info() {
        this->m_language = "";
        this->m_major = "";
        this->m_career = "";
        this->m_favour = "";
        this->m_score = -1;
    }

    Info(string language, string major, string career, string favour, int score) {
        this->m_language = language;
        this->m_major = major;
        this->m_career = career;
        this->m_favour = favour;
        this->m_score = score;
    }

    Info(string input) {
        if (input.size() == 0) {
            this->m_language = "";
            this->m_major = "";
            this->m_career = "";
            this->m_favour = "";
            this->m_score = -1;
            return;
        }
        
        vector<string> split_str = split(input, " ");
        if (split_str.size() != INFO_LEN) {
            this->m_language = "";
            this->m_major = "";
            this->m_career = "";
            this->m_favour = "";
            this->m_score = -1;
            return;
        }

        if (!(Info::verify_language(split_str[0]) && Info::verify_major(split_str[1]) && Info::verify_career(split_str[2]) && Info::verify_favour(split_str[3]))) {
            this->m_language = "";
            this->m_major = "";
            this->m_career = "";
            this->m_favour = "";
            this->m_score = -1;
            return;
        }
        int score;
        if (split_str[4] == "-") {
            score = -1;
        }
        else {
            try {
                score = stoi(split_str[4]);
            }
            catch (...) {
                this->m_language = "";
                this->m_major = "";
                this->m_career = "";
                this->m_favour = "";
                this->m_score = -1;
                return;
            }
        }

        this->m_language = split_str[0];
        this->m_major = split_str[1];
        this->m_career = split_str[2];
        this->m_favour = split_str[3];
        this->m_score = score;
    }

    bool operator==(Info& target) {
        bool rtn = (target.m_language == "-" || this->m_language == target.m_language) &&
            (target.m_major == "-" || this->m_major == target.m_major) &&
            (target.m_career == "-" || this->m_career == target.m_career) &&
            (target.m_favour == "-" || this->m_favour == target.m_favour) &&
            (target.m_score == -1 || this->m_score >= target.m_score);
        
        return rtn;
    }

    static bool verify_language(string input) {
        if (input.compare("cpp") == 0 || input.compare("java") == 0 || input.compare("python") == 0 || input.compare("-") == 0)
            return true;
        else
            return false;
    }

    static bool verify_major(string input) {
        if (input.compare("backend") == 0 || input.compare("frontend") == 0 || input.compare("-") == 0)
            return true;
        else
            return false;
    }

    static bool verify_career(string input) {
        if (input.compare("junior") == 0 || input.compare("senior") == 0 || input.compare("-") == 0)
            return true;
        else
            return false;
    }

    static bool verify_favour(string input) {
        if (input.compare("chicken") == 0 || input.compare("pizza") == 0 || input.compare("-") == 0)
            return true;
        else
            return false;
    }
};

vector<int> solution(vector<string> info, vector<string> query) {
    vector<int> answer;
    
    vector<Info> vec_info;
    vector<Info> vec_query;

    for (int i = 0; i < info.size(); i++) {
        string temp = info.at(i);

        Info info_trans = Info(temp);
        if (info_trans.m_language == "") {
            vector<int> error;
            return error;
        }
        vec_info.push_back(info_trans);
    }

    string replace_source = " and ";
    string replace_target = " ";
    for (int i = 0; i < query.size(); i++) {
        string temp = query.at(i);

        size_t t = temp.find(replace_source);
        while (t != string::npos) {
            temp.replace(t, replace_source.length(), replace_target);
            t = temp.find(replace_source);
        }
        Info info_trans = Info(temp);
        if (info_trans.m_language == "") {
            vector<int> error;
            return error;
        }
        vec_query.push_back(info_trans);
    }

    int cnt = 0;
    for (int i = 0; i < vec_query.size(); i++) {
        for (int j = 0; j < vec_info.size(); j++) {
            if (vec_info.at(j) == vec_query.at(i))
                cnt++;
        }
        answer.push_back(cnt);
        cnt = 0;
    }
    
    return answer;
}