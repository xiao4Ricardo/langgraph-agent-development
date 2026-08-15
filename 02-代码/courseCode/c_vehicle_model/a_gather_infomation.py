def getVictoriaStatus():
    return "凯瑞维多利亚2024年每月销售量及全年累计63272辆"

def getBenBenStatus():
    return "长安奔奔E-Star 2024年每月销售量及全年累计3749辆"

def getHaiouStatus():
    return "比亚迪海鸥 2024年每月销售量及全年累计403393辆"

def getKaolaStatus():
    return "北汽新能源考拉 2024年每月销售量及全年累计14733辆"

def getFemaleMarketTrend():
    return "面向女性客户的汽车品牌发展趋势：需求驱动、技术平权、社群共建。"

def getInfomation(state):
    state["victoriaStatus"] = getVictoriaStatus()
    state["competitorStatus"] = getBenBenStatus() + "\n" + getHaiouStatus() + "\n" + getKaolaStatus()
    state["femaleMarketTrend"] = getFemaleMarketTrend()
    return state