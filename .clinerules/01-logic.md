# 依照你從 context7 讀到你的知識撰寫 addons

## addons 名稱

- 名稱是 hr_expense_by_cline

## 繼承的 addons 以及增加的欄位

- 繼承 hr_expense 並且 增加一個 `ai_cline` 的 field, tree (`view_my_expenses_tree`) 和 form (`hr_expense_view_form`) 都要顯示 `ai_cline`, 位置都放在 `employee_id` 的後面.

## 增加按鈕並跳出 wizard

- 幫我在 `hr.expense` 的 form (`hr_expense_view_form`) 上, 增加一個 button 名稱是 "ai 按鈕", 位置放在 button(`action_view_sheet`) 後面, 點下去會跳一個 wizard, 預設會有 一個 `ai_date` date field, 當使用者可以自行選擇日期.

## 思考是否需要 `ir.model.access.csv`

## 確認全部的架構是否有 `__init__.py`, 以及是否有 import 對應的 model
