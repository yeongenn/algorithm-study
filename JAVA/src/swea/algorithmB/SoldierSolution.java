package JAVA.src.swea.algorithmB;

import java.util.ArrayList;

public class SoldierSolution {
    // List로 관리해야겠다고 생각
    // 제한시간 초과...!

    class Soldier {
        int mID, mScore;

        public Soldier (int mID, int mScore) {
            this.mID = mID;
            this.mScore = mScore;
        }
    }

    // 리스트
    ArrayList<Soldier> soldiers[];

    public void init() {
        soldiers = new ArrayList[6];    //  소속팀 (1 ≤ mTeam ≤ 5)
        for (int i = 1; i <= 5; i++) {
            soldiers[i] = new ArrayList<>();
        }
    }

    // 고유번호가 mID, 소속팀이 mTeam, 평판 점수가 mScore
    public void hire(int mID, int mTeam, int mScore) {
        if (soldiers[mTeam].size() == 0) {
            soldiers[mTeam].add(new Soldier(mID, mScore));
            return;
        }
        int left = 0;
        int right = soldiers[mTeam].size() - 1;
        int middle = 0;

        while (left <= right) {
            middle = (left + right) / 2;
            if (soldiers[mTeam].get(middle).mID > mID) {
                left = middle + 1;
                continue;
            }
            right = middle - 1;
        }
        if (middle > right) {
            soldiers[mTeam].add(middle, new Soldier(mID, mScore));
        } else {
            soldiers[mTeam].add(middle + 1, new Soldier(mID, mScore));
        }
    }

    public void fire(int mID) {
        for (int i = 1; i <= 5; i++) {
            int left = 0;
            int right = soldiers[i].size() - 1;
            int middle = 0;
            while (left <= right) {
                middle = (left + right) / 2;
                if (soldiers[i].get(middle).mID == mID) {
                    soldiers[i].remove(middle);
                    return;
                } else if (soldiers[i].get(middle).mID > mID) {
                    left = middle + 1;
                    continue;
                }
                right = middle - 1;
            }
        }
    }

    public void updateSoldier(int mID, int mScore) {
        for (int i = 1; i <= 5; i++) {
            int left = 0;
            int right = soldiers[i].size() - 1;
            int middle = 0;
            while (left <= right) {
                middle = (left + right) / 2;
                if (soldiers[i].get(middle).mID == mID) {
                    soldiers[i].get(middle).mScore = mScore;
                    return;
                } else if (soldiers[i].get(middle).mID > mID) {
                    left = middle + 1;
                    continue;
                }
                right = middle - 1;
            }
        }
    }

    // 소속팀이 mTeam인 병사들의 평판 점수 모두 변경
    public void updateTeam(int mTeam, int mChangeScore) {
        int score;
        for (Soldier s : soldiers[mTeam]) {
            score = s.mScore + mChangeScore;
            if (score > 5) {
                s.mScore = 5;
            } else if (score < 1) {
                s.mScore = 1;
            } else {
                s.mScore = score;
            }
        }
    }

    // 평판 점수가 가장 높은 병사 고유번호 반환
    // 여러 명일 경우, 가장 큰 고유번호 반환
    public int bestSoldier(int mTeam) {
        int score = Integer.MIN_VALUE;
        int id = Integer.MAX_VALUE;
        for (Soldier s : soldiers[mTeam]) {
            if (score < s.mScore) {
                score = s.mScore;
                id = s.mID;
            } else if (score == s.mScore) {
                if (id < s.mID) {
                    score = s.mScore;
                    id = s.mID;
                }
            }
        }
        return id;
    }
}
