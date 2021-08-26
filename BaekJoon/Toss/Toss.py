import sys
sys.stdin = open('../input.txt', 'r')
# import math
# def solution(orderAmount, taxFreeAmount, serviceFee):
#     # orderAmount : 주문금액
#     # taxFreeAmount : 비과세금액
#     # serviceFee : 봉사료
#
#     #공급대가
#     provide = orderAmount-serviceFee
#     tax = math.ceil(provide/10)
#     # 공급가액
#     price = provide-tax
#     # 과세금액
#     taxPrice = price-taxFreeAmount
#
#     if provide - taxFreeAmount == 1: return 0
#
#     return tax
#
#
#
#
#
#
#     provide = None
#     if serviceFee:
#         provide = orderAmount - serviceFee
#         taxAmount = provide - taxFreeAmount
#         tax = math.ceil(taxAmount / 10)
#     else:
#         taxAmount = orderAmount - taxFreeAmount
#         tax = math.ceil(taxAmount/10)
#         provide = orderAmount+tax
#
#     if provide - taxFreeAmount == 1: return 0
#     return tax