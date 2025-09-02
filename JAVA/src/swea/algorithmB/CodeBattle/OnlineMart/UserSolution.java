package JAVA.src.swea.algorithmB.CodeBattle.OnlineMart;

import java.util.HashMap;
import java.util.Map;
import java.util.TreeSet;

public class UserSolution {
    int[][] diff;   // 가격 변화 저장
    Map<Integer, Product> products;
    TreeSet<Product>[][] productSet = new TreeSet[6][6];    // 인덱스 맞추기

    public void init() {
        diff = new int[6][6];
        products = new HashMap<>();
        for (int category = 1; category <= 5; category++) {
            for (int company = 1; company <= 5; company++) {
                productSet[category][company] = new TreeSet<>();
            }
        }

        return;
    }

    public int sell(int mID, int mCategory, int mCompany, int mPrice) {
//        Product product = new Product(mID, mCategory, mCompany, mPrice);
        Product product = new Product(mID, mCategory, mCompany, mPrice - diff[mCategory][mCompany]);    // 가격 변화 반영하기
        products.put(mID, product);
        productSet[mCategory][mCompany].add(product);

        return productSet[mCategory][mCompany].size();
    }

    public int closeSale(int mID) {
        if (!products.containsKey(mID)) {
            return -1;
        }

        Product product = products.get(mID);
        products.remove(mID);
        // 트리셋에서도 삭제하기
        productSet[product.category][product.company].remove(product);

        // 판매 종료 시 상품 가격 반환
        return product.price + diff[product.category][product.company];
    }

    public int discount(int mCategory, int mCompany, int mAmount) {
        // 가격 변화 배열 수정하기
        diff[mCategory][mCompany] -= mAmount;

        // 낮춘 가격이 0이거나 음수가 되면 해당 상품은 판매 종료 - 1: Runtime Error
//        for (Product product : productSet[mCategory][mCompany]) {
//            if (product.price + diff[mCategory][mCompany] <= 0) {
//                products.remove(product.id);
//                productSet[mCategory][mCompany].remove(product);
//            }
//        }

        // 낮춘 가격이 0이거나 음수가 되면 해당 상품은 판매 종료 - 2: Pass
        while (!productSet[mCategory][mCompany].isEmpty()
                && productSet[mCategory][mCompany].first().price + diff[mCategory][mCompany] <= 0) {
            products.remove(productSet[mCategory][mCompany].first().id);
            productSet[mCategory][mCompany].pollFirst();
        }

        // 해당 품목, 제조사가 판매 중인 상품 개수
        return productSet[mCategory][mCompany].size();
    }

    // 조건 만족하는 상품 중 가격이 낮은 순서대로 최대 5개 상품 반환
    Solution.RESULT show(int mHow, int mCode) {
        Solution.RESULT res = new Solution.RESULT();
        TreeSet<Product> recommand = new TreeSet<>();

        for (int category = 1; category <= 5; category++) {
            if (mHow == 1 && category != mCode) {       // mHow == 1
                continue;
            }
            for (int company = 1; company <= 5; company++) {
                if (productSet[category][company].isEmpty()
                        || mHow == 2 && company != mCode) {     // mHow == 0, mHow == 2
                    continue;
                }
                Product product = productSet[category][company].first();
                while (product != null) {
                    int price = product.price + diff[category][company];
                    if (recommand.size() < 5) {
                        recommand.add(new Product(product.id, category, company, price));
                    } else {
                        int prevId = recommand.last().id;
                        int prevPrice = recommand.last().price;

                        if (prevPrice < price || (prevPrice == price && prevId < product.id)) {
                            break;
                        }
                        recommand.pollLast();
                        recommand.add(new Product(product.id, category, company, price));
                    }

                    product = productSet[category][company].higher(product);
                }
            }
        }

        res.cnt = 0;
        while (!recommand.isEmpty()) {
            res.IDs[res.cnt++] = recommand.pollFirst().id;
        }

        return res;
    }

    static class Product implements Comparable<Product> {
        int id;
        int category;
        int company;
        int price;

        public Product(int id, int category, int company, int price) {
            this.id = id;
            this.category = category;
            this.company = company;
            this.price = price;
        }

        @Override
        public int compareTo(Product o) {
            // 정렬 기준 : id - price
            return this.price == o.price ? this.id - o.id : this.price - o.price;
        }
    }

}
