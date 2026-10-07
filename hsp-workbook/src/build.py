# -*- coding: utf-8 -*-
"""HSPの働き方ゼミ｜働き方の取扱説明書 ワークブック HTML生成"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = "file://" + os.path.join(HERE, "fonts", "NotoSansJP.ttf")

TITLE = "HSPの働き方ゼミ｜働き方の取扱説明書"

STEPS = {
    1: ("STEP1", "自分を知る", "s1"),
    2: ("STEP2", "今を整える", "s2"),
    3: ("STEP3", "これからを選ぶ", "s3"),
    "F": ("最終版", "私の働き方の取扱説明書", "sf"),
}

pages = []


def page(body, step=None, cls="", footer=True):
    pages.append((body, step, cls, footer))


# ---------- 部品 ----------
def lines(n, h=8.5, cls=""):
    return f'<div class="lines {cls}">' + f'<div style="height:{h}mm"></div>' * n + '</div>'


def field(label, n=3, h=8.5, hint=""):
    hint_html = f'<span class="hint">{hint}</span>' if hint else ""
    return f'<div class="field"><div class="flabel">{label}{hint_html}</div>{lines(n, h)}</div>'


def numbered(n, start=1, h=9.5, cls=""):
    rows = "".join(f'<div class="nrow" style="height:{h}mm"><span class="num">{i}</span></div>' for i in range(start, start + n))
    return f'<div class="numbered {cls}">{rows}</div>'


def work_head(step, no, title, purpose, part=None):
    lab, name, c = STEPS[step]
    part_html = f'<span class="part">{part}</span>' if part else ""
    purpose_html = (
        f'<div class="purpose"><span class="tag">このワークの目的</span><p>{purpose}</p></div>' if purpose else ""
    )
    return (
        f'<div class="whead"><div class="wno">ワーク<b>{no}</b></div>'
        f'<div class="wtitle"><div class="wstep">{lab}｜{name}</div><h2>{title}{part_html}</h2></div></div>'
        + purpose_html
    )


def explain(text, title="考えるためのヒント"):
    return f'<div class="explain"><div class="etitle">{title}</div>{text}</div>'


def example(html, title="記入例"):
    return f'<div class="example"><span class="extag">{title}</span>{html}</div>'


def summary(html):
    return f'<div class="summary"><div class="stitle">まとめ</div>{html}</div>'


def reflect(target, html):
    return (
        f'<div class="reflect"><div class="rhead"><span class="ricon">▶</span>取扱説明書に反映する内容'
        f'<span class="rtarget">反映先：{target}</span></div>{html}</div>'
    )


def q(label):
    return f'<div class="qlabel"><span class="qmark">Q</span>{label}</div>'


def chips(items):
    return '<div class="chips">' + "".join(f"<span>{i}</span>" for i in items) + "</div>"


def checks(items, cols=4):
    return f'<div class="checks" style="grid-template-columns:repeat({cols},1fr)">' + "".join(
        f'<span><i class="box"></i>{i}</span>' for i in items
    ) + "</div>"


def circles(n=5):
    return '<span class="circles">' + "".join(f"<i>{i}</i>" for i in range(1, n + 1)) + "</span>"


def divider(step):
    lab, name, c = STEPS[step]
    return c


# =====================================================================
# 1. 表紙
# =====================================================================
page(
    """
<div class="cover">
  <div class="cover-band"></div>
  <div class="cover-inner">
    <div class="cover-brand">HSPの働き方ゼミ</div>
    <h1 class="cover-title">働き方の<br>取扱説明書</h1>
    <div class="cover-rule"></div>
    <p class="cover-sub">3STEP・推奨3か月で<br>「自分に合った働き方」を言語化するワークブック</p>
    <div class="cover-steps">
      <div class="cs s1"><b>STEP1</b><span>自分を知る</span></div>
      <div class="cs-arrow">›</div>
      <div class="cs s2"><b>STEP2</b><span>今を整える</span></div>
      <div class="cs-arrow">›</div>
      <div class="cs s3"><b>STEP3</b><span>これからを選ぶ</span></div>
      <div class="cs-arrow">›</div>
      <div class="cs sf"><b>最終版</b><span>取扱説明書</span></div>
    </div>
    <div class="cover-name">
      <div><span>名前</span><i></i></div>
      <div><span>はじめた日</span><i></i></div>
    </div>
  </div>
  <div class="cover-ver">Version 1.0</div>
</div>
""",
    cls="p-cover",
    footer=False,
)

# =====================================================================
# 2. はじめに
# =====================================================================
page(
    """
<div class="sec-label">INTRODUCTION</div>
<h2 class="sec-title">はじめに</h2>
<div class="intro">
  <p class="lead">「仕事がしんどい。<br>でも、辞めるべきか分からない。」</p>
  <p>そんな状態になると、<br>「我慢して働き続ける」か「会社を辞める」か、<br>の二択で考えてしまいがちです。</p>
  <p>でも、本当に必要なのは、<br><b class="mark">自分に合った働き方の判断基準を持つこと</b>です。</p>
  <p>このワークブックでは、次のことを少しずつ整理します。</p>
  <ul class="intro-list">
    <li>自分は何に疲れるのか</li>
    <li>どんな環境なら働きやすいのか</li>
    <li>どこまでなら頑張れるのか</li>
    <li>何を断った方がいいのか</li>
    <li>どんな職場は避けたいのか</li>
  </ul>
  <p>そして最後に、<b>「自分の働き方の取扱説明書」</b>を完成させます。</p>
  <div class="intro-goal">
    <p>正解を出すことが目的ではありません。</p>
    <p>今の自分にとって、どんな働き方が合っているのか。<br>その判断材料を、<b>自分の言葉で持つこと</b>がゴールです。</p>
  </div>
</div>
""",
)

# =====================================================================
# 3. 使い方
# =====================================================================
page(
    """
<div class="sec-label">HOW TO USE</div>
<h2 class="sec-title">このワークブックの使い方</h2>
<p class="sec-lead">疲れているときほど、「ちゃんとやらなきゃ」と思いがちです。<br>このワークブックは、<b>ゆるく・少しずつ</b>進めることを前提につくっています。</p>
<div class="rules">
  <div class="rule"><span class="ri">1</span><div><b>全部を一気に埋めなくて大丈夫</b><p>今日はこの1問だけ、でも十分な前進です。</p></div></div>
  <div class="rule"><span class="ri">2</span><div><b>1回15〜30分程度でOK</b><p>疲れを感じたら、そこで閉じてください。</p></div></div>
  <div class="rule"><span class="ri">3</span><div><b>空欄があっても次へ進んでOK</b><p>あとから思いつくことも多いので、気にせず先へ。</p></div></div>
  <div class="rule"><span class="ri">4</span><div><b>推奨期間は約3か月</b><p>1STEPにつき約1か月が目安です。早くても遅くても構いません。</p></div></div>
  <div class="rule"><span class="ri">5</span><div><b>答えは途中で変わってOK</b><p>書き直しは「考えが深まった」証拠です。</p></div></div>
  <div class="rule"><span class="ri">6</span><div><b>半年後・1年後に見直してOK</b><p>巻末の「見直し・更新ページ」を使ってください。</p></div></div>
</div>
<div class="howto-sub">
  <div class="hs-title">各ワークの流れ（共通フォーマット）</div>
  <div class="fmt">
    <span>① 目的</span><span>② ヒント</span><span>③ 質問</span><span>④ 記入</span><span class="fmt-ex">⑤ 記入例</span><span>⑥ まとめ</span><span class="fmt-r">⑦ 取扱説明書に反映</span>
  </div>
  <p class="small">⑤の<b>「記入例」</b>は薄いグレーの枠で表示しています。あくまで一例なので、表現や量は自由に。<br>⑦の<b>「取扱説明書に反映する内容」</b>が、最終版のページにそのままつながります。</p>
</div>
<div class="howto-sub">
  <div class="hs-title">スプレッドシート版との使い分け</div>
  <div class="two">
    <div class="mini"><b>スプレッドシート版</b><p>書き込み・更新するメイン教材。見直しや修正がしやすい。</p></div>
    <div class="mini"><b>このPDF版</b><p>印刷して、紙に書きながらじっくり考えたいとき用。ワーク名・順番は同じです。</p></div>
  </div>
</div>
""",
)

# =====================================================================
# 4. 全体の流れ
# =====================================================================
page(
    """
<div class="sec-label">ROADMAP</div>
<h2 class="sec-title">全体の流れ（推奨3か月）</h2>
<div class="flow">
  <div class="fstep s1">
    <div class="fmonth">1か月目</div>
    <div class="fbody"><div class="fname"><b>STEP1</b>自分を知る</div><div class="ftheme">なぜ私は仕事で消耗するのか？</div>
    <div class="fworks">ワーク1 働き方セルフチェック／ワーク2 消耗ポイントマップ／ワーク3 働きやすい条件／ワーク4 頑張りすぎパターン</div></div>
  </div>
  <div class="farrow">▼</div>
  <div class="fstep s2">
    <div class="fmonth">2か月目</div>
    <div class="fbody"><div class="fname"><b>STEP2</b>今を整える</div><div class="ftheme">今の職場でもう少しラクに働けないか？</div>
    <div class="fworks">ワーク5 変えられること・変えられないこと／ワーク6 仕事の境界線／ワーク7 相談ルート</div></div>
  </div>
  <div class="farrow">▼</div>
  <div class="fstep s3">
    <div class="fmonth">3か月目</div>
    <div class="fbody"><div class="fname"><b>STEP3</b>これからを選ぶ</div><div class="ftheme">残る・辞める・転職するをどう判断するか？</div>
    <div class="fworks">ワーク8 残る・環境を変える判断基準／ワーク9 Must・Want・NG／ワーク10 90日行動計画</div></div>
  </div>
  <div class="farrow">▼</div>
  <div class="fstep sf">
    <div class="fmonth">仕上げ</div>
    <div class="fbody"><div class="fname"><b>最終版</b>私の働き方の取扱説明書を完成</div><div class="ftheme">これまでの「取扱説明書に反映する内容」を1つにまとめる</div></div>
  </div>
</div>
<div class="sched">
  <div class="hs-title">私の進行予定（書き込み用）</div>
  <table class="tbl sched-tbl">
    <tr><th>STEP</th><th>開始予定日</th><th>終了予定日</th><th>完了チェック</th></tr>
    <tr><td>STEP1｜自分を知る</td><td>　　月　　日</td><td>　　月　　日</td><td class="c"><i class="box"></i></td></tr>
    <tr><td>STEP2｜今を整える</td><td>　　月　　日</td><td>　　月　　日</td><td class="c"><i class="box"></i></td></tr>
    <tr><td>STEP3｜これからを選ぶ</td><td>　　月　　日</td><td>　　月　　日</td><td class="c"><i class="box"></i></td></tr>
    <tr><td>最終版｜取扱説明書</td><td>　　月　　日</td><td>　　月　　日</td><td class="c"><i class="box"></i></td></tr>
  </table>
</div>
""",
)


# =====================================================================
# STEP扉
# =====================================================================
def step_door(step, month, theme, desc, works):
    lab, name, c = STEPS[step]
    wl = "".join(f"<li><span>{a}</span>{b}</li>" for a, b in works)
    page(
        f"""
<div class="door">
  <div class="door-month">{month}</div>
  <div class="door-lab">{lab}</div>
  <h2 class="door-name">{name}</h2>
  <div class="door-theme"><span>テーマ</span>{theme}</div>
  <p class="door-desc">{desc}</p>
  <ul class="door-works">{wl}</ul>
</div>
""",
        step=step,
        cls="p-door",
    )


step_door(
    1,
    "推奨：1か月目",
    "なぜ私は仕事で消耗するのか？",
    "まずは「今の自分」を知るところから。<br>何に疲れて、どんなときに働きやすくて、どんなときに頑張りすぎてしまうのか。<br>良い・悪いの評価はせず、事実をそのまま書き出していきます。",
    [("ワーク1", "働き方セルフチェック"), ("ワーク2", "消耗ポイントマップ"), ("ワーク3", "働きやすい条件"), ("ワーク4", "頑張りすぎパターン")],
)

# ---------------- ワーク1 ----------------
W1_ITEMS = [
    "仕事が終わっても頭から仕事が離れない",
    "休日になっても疲れが抜けない",
    "頼まれた仕事を断るのが苦手",
    "周囲の機嫌や評価が気になる",
    "仕事を抱え込みやすい",
    "周囲が忙しいと自分だけ帰りにくい",
    "急な予定変更が続くと疲れる",
    "マルチタスクが続くと消耗する",
    "静かな環境の方が集中しやすい",
    "頑張りすぎてから「無理していた」と気づく",
    "今の働き方をこの先も続けられるか不安",
    "転職したいと思うことがある",
    "自分に合う職場の条件が分からない",
    "休むタイミングが分からない",
    "「もっと頑張らないと」と思いがち",
]
rows = "".join(
    f'<tr><td class="n">{i}</td><td class="qt">{t}</td>' + "".join('<td class="c"><i class="ci"></i></td>' for _ in range(5)) + "</tr>"
    for i, t in enumerate(W1_ITEMS, 1)
)
page(
    work_head(1, 1, "働き方セルフチェック", "現在の働き方の状態を振り返る。")
    + explain(
        "<p>直感で、いちばん近いものに○をつけてください。点数の合計や診断はしません。<br>「自分はこういう傾向があるんだな」と気づくための<b>振り返りシート</b>です。</p>"
    )
    + f"""
<table class="tbl check-tbl">
  <tr><th></th><th class="qt">質問</th><th>まったく<br>当てはまらない</th><th>あまり<br>当てはまらない</th><th>どちらとも<br>いえない</th><th>少し<br>当てはまる</th><th>とても<br>当てはまる</th></tr>
  {rows}
</table>
""",
    step=1,
)
page(
    work_head(1, 1, "働き方セルフチェック", None, "（2/2）")
    + q("今の働き方で、特に気になったことは？")
    + '<p class="qnote">「とても当てはまる」「少し当てはまる」をつけた項目を見返して、気づいたことを書いてみましょう。</p>'
    + lines(10)
    + example(
        "<p>「頼まれた仕事を断るのが苦手」「頑張りすぎてから気づく」が“とても当てはまる”だった。<br>"
        "引き受けすぎて、気づいたら休日まで疲れを持ち越している気がする。</p>"
    )
    + summary(
        "<p>ここで気になった項目は、このあとのワークで深掘りするヒントになります。</p>"
        + '<div class="kv"><span>特に深掘りしたい項目（番号）</span><i class="uline"></i></div>'
    )
    + reflect(
        "消耗しやすい条件／頑張りすぎる3つのパターン（ワーク2・4で整理）",
        "<p>気になった項目を、ワーク2〜4で具体的に掘り下げるテーマとしてメモしておきましょう。</p>"
        + '<div class="kv"><span>ワーク2〜4で掘り下げたいテーマ</span></div>'
        + lines(2),
    ),
    step=1,
)

# ---------------- ワーク2 ----------------
W2_ELEMS = ["仕事内容", "仕事量", "人間関係", "音・環境", "電話", "突発対応", "マルチタスク", "責任", "評価", "残業", "通勤", "その他（　　　）"]
page(
    work_head(1, 2, "消耗ポイントマップ", "「私は何に疲れているのか？」を整理する。", "（1/3）")
    + explain(
        "<p>「なんとなく疲れる」を、<b>場面</b>と<b>要素</b>に分けて見ていきます。<br>"
        "疲れの原因が分かると、「何を避ければいいか」「何を変えればいいか」が見えてきます。</p>"
        "<p>最近1〜2週間で、特に疲れた場面を思い出してください。大きな出来事でなくて構いません。</p>"
    )
    + '<div class="hs-title">疲れた要素の例</div>'
    + chips(W2_ELEMS)
    + example(
        """
<table class="extbl">
<tr><th>最近特に疲れた場面</th><td>月曜の午前、会議の資料作成中</td></tr>
<tr><th>何が起きた？</th><td>集中したい時に電話が3本続き、そのたびに作業が中断した。</td></tr>
<tr><th>特に疲れた要素</th><td>電話／突発対応／マルチタスク</td></tr>
<tr><th>疲労度（1〜5）</th><td>4</td></tr>
<tr><th>次回どうしたい？</th><td>集中作業の時間だけ、電話番を同僚と交代してもらえないか相談する。</td></tr>
</table>"""
    )
    + q("最近1〜2週間で「疲れたな」と感じた場面を、思いつくまま書き出してみましょう")
    + '<p class="qnote">メモ程度で大丈夫です。この中から3つを選んで、次のページで詳しく振り返ります。</p>'
    + lines(6),
    step=1,
)


def w2_card(no):
    return f"""
<div class="card scene">
  <div class="card-h">場面 {no}</div>
  <div class="sg">
    <div class="sl">最近特に疲れた場面</div><div class="sv">{lines(1, 9)}</div>
    <div class="sl">何が起きた？</div><div class="sv">{lines(2, 9)}</div>
    <div class="sl">特に疲れた要素</div><div class="sv">{checks(W2_ELEMS, 6)}</div>
    <div class="sl">疲労度</div><div class="sv lvl">軽い {circles()} 重い</div>
    <div class="sl">次回どうしたい？</div><div class="sv">{lines(1, 9)}</div>
  </div>
</div>"""


page(work_head(1, 2, "消耗ポイントマップ", None, "（2/3）") + w2_card(1) + w2_card(2) + w2_card(3), step=1)
page(
    work_head(1, 2, "消耗ポイントマップ", None, "（3/3）")
    + summary(
        "<p>書き出した場面を見返して、繰り返し出てくる要素や、疲労度の高い要素に注目しましょう。</p>"
        '<div class="hs-title">私が消耗しやすい条件 TOP5</div>' + numbered(5, h=13)
    )
    + example("<p>1. 集中作業中に何度も中断される　2. 電話対応が続く　3. 急な予定変更が重なる</p>")
    + reflect(
        "私が消耗しやすい条件 TOP5／次の職場のNG条件",
        "<p><b>私が避けたい・注意したい条件は？</b>（1〜3個）</p>" + numbered(3, h=13),
    ),
    step=1,
)

# ---------------- ワーク3 ----------------
W3_CONDS = ["静かな環境", "一人で集中する時間", "明確な指示", "裁量がある", "残業が少ない", "人間関係が穏やか", "電話が少ない", "リモートワーク", "通勤時間が短い", "突発対応が少ない", "仕事量が一定", "評価基準が明確"]
page(
    work_head(1, 3, "働きやすい条件", "「私はどんな環境なら働きやすいのか？」を整理する。", "（1/3）")
    + explain(
        "<p>疲れる条件の裏側には、<b>「こうだったらラク」という条件</b>が隠れています。<br>"
        "今の職場だけでなく、過去の職場、アルバイト、学生時代などの経験も手がかりになります。</p>"
    )
    + q("比較的ラクに働けた日は？")
    + lines(4)
    + q("その日は何が良かった？")
    + lines(5)
    + q("過去の職場で居心地が良かった部分は？")
    + lines(5)
    + q("集中しやすかった環境は？")
    + lines(4),
    step=1,
)
page(
    work_head(1, 3, "働きやすい条件", None, "（2/3）")
    + '<p class="qnote">次の観点で、あなたにとって「ちょうどいい」状態を書いてみましょう。</p>'
    + '<div class="grid2">'
    + f'<div class="card">{q("人との距離感は？")}{lines(5, 8)}</div>'
    + f'<div class="card">{q("仕事量は？")}{lines(5, 8)}</div>'
    + f'<div class="card">{q("裁量は？")}{lines(5, 8)}</div>'
    + f'<div class="card">{q("通勤や勤務時間は？")}{lines(5, 8)}</div>'
    + "</div>"
    + '<div class="hs-title">当てはまる条件にチェック（条件例）</div>'
    + checks(W3_CONDS, 3)
    + '<div class="kv"><span>その他の条件</span><i class="uline"></i></div>'
    + example(
        "<p><b>比較的ラクに働けた日：</b>在宅勤務で、午前中に資料作成だけに集中できた日。<br>"
        "<b>何が良かった？：</b>話しかけられず、電話もなく、自分のペースで進められた。<br>"
        "<b>人との距離感：</b>必要なときに相談できれば、雑談は少なめがちょうどいい。</p>"
    ),
    step=1,
)
page(
    work_head(1, 3, "働きやすい条件", None, "（3/3）")
    + summary(
        "<p>チェックした条件と、書き出した内容を見比べて、特に大事なものを5つ選びましょう。</p>"
        '<div class="hs-title">私が働きやすい条件 TOP5</div>' + numbered(5, h=13)
    )
    + example("<p>1. 一人で集中する時間がある　2. 仕事量が一定　3. 評価基準が明確</p>")
    + reflect(
        "私が働きやすい条件 TOP5／次の職場のMust条件",
        "<p>TOP5の中で、<b>「これがないと長く働けない」</b>と思うものに◎をつけておきましょう。<br>STEP3のワーク9（Must条件）を考えるときの材料になります。</p>"
        '<div class="kv"><span>◎をつけた条件</span></div>' + lines(3),
    ),
    step=1,
)

# ---------------- ワーク4 ----------------
page(
    work_head(1, 4, "頑張りすぎパターン", "自分が無理を始めるパターンを知る。", "（1/3）")
    + explain(
        "<p>頑張りすぎは、ある日突然ではなく、<b>いつも似たきっかけ</b>から始まることが多いものです。<br>"
        "「状況 → 考え → 行動 → 結果」の流れで振り返ると、自分のパターンが見えてきます。</p>"
        "<p>自分を責めるためではなく、<b>早めに気づくため</b>のワークです。</p>"
    )
    + '<div class="hs-title">よくある頑張りすぎパターンの例</div>'
    + checks(
        [
            "頼まれると断れない",
            "周囲が残業していると帰れない",
            "期待されると無理して応えようとする",
            "ミスが怖くて必要以上に確認する",
            "評価が下がることを恐れて仕事を抱え込む",
            "その他（　　　　　　　　）",
        ],
        2,
    )
    + q("最近「無理していたな」と感じた出来事は？（思いつくままメモ）")
    + lines(3)
    + '<div class="flow5"><span>状況</span>›<span>考え</span>›<span>行動</span>›<span>結果</span>›<span>次から</span></div>'
    + example(
        """
<table class="extbl">
<tr><th>どんな状況だった？</th><td>締め切り前日の夕方、上司から別の資料作成を頼まれた。</td></tr>
<tr><th>そのとき何を考えた？</th><td>「断ったら頼りにならないと思われる」</td></tr>
<tr><th>どんな行動を取った？</th><td>「大丈夫です」と引き受け、22時まで残業した。</td></tr>
<tr><th>結果どうなった？</th><td>翌日の本来の仕事でミスが出て、週末は寝込んだ。</td></tr>
<tr><th>次からどうしたい？</th><td>「今日中は難しいので、明日の午後でもいいですか」と期限を相談する。</td></tr>
</table>"""
    ),
    step=1,
)


def w4_card(no):
    items = ["どんな状況だった？", "そのとき何を考えた？", "どんな行動を取った？", "結果どうなった？", "次からどうしたい？"]
    inner = "".join(f'<div class="sl">{t}</div><div class="sv">{lines(2, 9)}</div>' for i, t in enumerate(items))
    return f'<div class="card scene"><div class="card-h">パターン {no}</div><div class="sg">{inner}</div></div>'


page(work_head(1, 4, "頑張りすぎパターン", None, "（2/3）") + w4_card(1) + w4_card(2), step=1)
page(
    work_head(1, 4, "頑張りすぎパターン", None, "（3/3）")
    + summary(
        "<p>書き出した内容から、「またこれをやっている」と感じるパターンを3つにまとめましょう。<br>"
        "<span class='small'>例：「〇〇なとき、△△と考えて、□□してしまう」</span></p>"
        '<div class="hs-title">私が頑張りすぎ始める3つのパターン</div>' + numbered(3, h=18)
    )
    + example("<p>1. 締め切り前に追加の依頼が来ると、断ったら評価が下がると考えて、残業してでも引き受けてしまう。</p>")
    + reflect(
        "私が頑張りすぎる3つのパターン",
        "<p>それぞれのパターンに気づくための<b>「サイン」</b>を書いておきましょう。</p>"
        '<div class="kv"><span>私の「頑張りすぎ」のサイン</span></div>'
        + lines(4)
        + '<p class="small">例：「大丈夫です」が口ぐせになる／昼休みを削り始める／寝る前に仕事のことを考える</p>',
    ),
    step=1,
)

# =====================================================================
# STEP2
# =====================================================================
step_door(
    2,
    "推奨：2か月目",
    "今の職場でもう少しラクに働けないか？",
    "「辞める・辞めない」を決める前に、今の職場でできる工夫を試してみます。<br>"
    "変えられること・相談すれば変わること・変えにくいことを分けて、<br>自分を守るためのルールと、ひとりで抱え込まない仕組みをつくります。",
    [("ワーク5", "変えられること・変えられないこと"), ("ワーク6", "仕事の境界線"), ("ワーク7", "相談ルート")],
)

# ---------------- ワーク5 ----------------
page(
    work_head(2, 5, "変えられること・変えられないこと", "今の職場で改善できることを整理する。", "（1/2）")
    + explain(
        "<p>しんどさの原因を、次の<b>3つの箱</b>に分けてみましょう。<br>"
        "すべてを変える必要はありません。<b>変えられる部分から少しずつ</b>手をつけるのがポイントです。</p>"
    )
    + '<div class="hs-title">検討例</div>'
    + chips(["仕事の進め方", "仕事量", "上司との関係", "部署", "通勤", "会社文化", "給与制度", "残業", "座席", "電話対応", "業務内容"])
    + f"""
<div class="box3">
  <div class="b3 b3a"><div class="b3h">自分で<br>変えられること</div>{lines(15, 8.5)}</div>
  <div class="b3 b3b"><div class="b3h">相談すれば<br>変わる可能性があること</div>{lines(15, 8.5)}</div>
  <div class="b3 b3c"><div class="b3h">自分では<br>変えにくいこと</div>{lines(15, 8.5)}</div>
</div>""",
    step=2,
)
page(
    work_head(2, 5, "変えられること・変えられないこと", None, "（2/2）")
    + example(
        """
<div class="ex3">
<div><b>自分で変えられること</b><p>集中作業を午前に寄せる／タスクを書き出してから始める</p></div>
<div><b>相談すれば変わる可能性があること</b><p>電話当番のローテーション／座席を通路側から移動</p></div>
<div><b>自分では変えにくいこと</b><p>会社の給与制度／全社的な会議文化</p></div>
</div>"""
    )
    + summary(
        "<p>「自分で変えられること」「相談すれば変わる可能性があること」の中から、<b>小さく試せること</b>を選びましょう。</p>"
        '<div class="hs-title">今月まず変えてみること（1〜3個）</div>' + numbered(3, h=15)
    )
    + reflect(
        "今の会社に残れる条件／これから90日でやること",
        "<p>ここで分かった<b>「これが変われば、今の会社でも続けられそう」</b>という条件を書いておきましょう。</p>" + lines(5)
        + '<p class="small">「自分では変えにくいこと」の中に、どうしても我慢できないものがあれば、STEP3で判断材料として使います。</p>',
    ),
    step=2,
)

# ---------------- ワーク6 ----------------
page(
    work_head(2, 6, "仕事の境界線", "自分を守るための働き方ルールをつくる。", "（1/2）")
    + explain(
        "<p>境界線とは、<b>「ここまでは引き受ける・ここからは守る」</b>という自分なりの線引きです。<br>"
        "疲れているときに考えると、つい「もう少し頑張れる」と判断してしまいます。<br>だからこそ、<b>元気なときに先に決めておく</b>ことが大切です。</p>"
    )
    + f"""
<div class="bound b-go"><div class="bh"><b>頑張る基準</b><span>どんな状態なら頑張っても大丈夫か？</span></div>{lines(5)}</div>
<div class="bound b-talk"><div class="bh"><b>断る基準</b><span>どんな仕事は断る・相談するか？</span></div>{lines(5)}</div>
<div class="bound b-stop"><div class="bh"><b>休む基準</b><span>どんなサインが出たら一度立ち止まるか？</span></div>{lines(5)}</div>
""",
    step=2,
)
page(
    work_head(2, 6, "仕事の境界線", None, "（2/2）")
    + example(
        "<p><b>頑張る基準：</b>睡眠が6時間以上とれていて、繁忙期が2週間以内に終わる見込みがあるとき。<br>"
        "<b>断る基準：</b>今週すでに残業が5時間を超えているときの追加依頼は、まず期限を相談する。<br>"
        "<b>休む基準：</b>休日に仕事の夢を見る・日曜の夕方に動悸がする状態が2週続いたら、有休を取る。</p>"
    )
    + summary(
        "<p>3つの基準をもとに、<b>「迷ったらこうする」</b>という形のルールにまとめましょう。<br>"
        "<span class='small'>例：「即答しない。『確認して15時までに返事します』と伝える」</span></p>"
        '<div class="hs-title">私を守る5つの働き方ルール</div>' + numbered(5, h=15)
    )
    + reflect(
        "私を守る5つの働き方ルール",
        "<p>5つのルールは、最終版の取扱説明書にそのまま書き写します。<br>職場で見返せるように、スマホのメモや手帳に入れておくのもおすすめです。</p>"
        '<div class="kv"><span>ルールを置いておく場所</span><i class="uline"></i></div>',
    ),
    step=2,
)

# ---------------- ワーク7 ----------------
page(
    work_head(2, 7, "相談ルート", "ひとりで抱え込まない仕組みをつくる。", "（1/2）")
    + explain(
        "<p>しんどいときほど、「誰に・いつ・どう話すか」を考える余裕がなくなります。<br>"
        "<b>困ったときの連絡先を先に決めておく</b>だけで、抱え込みを防ぎやすくなります。</p>"
    )
    + '<div class="hs-title">相談先の例</div>'
    + chips(["上司", "同僚", "人事", "家族", "友人", "外部相談窓口", "医療・心理・キャリア等の専門家"])
    + """
<table class="tbl route-tbl">
<tr><th>困ったこと</th><th>誰に相談する？</th><th>いつ相談する？</th><th>どう伝える？</th></tr>
<tr><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td></tr>
</table>""",
    step=2,
)
page(
    work_head(2, 7, "相談ルート", None, "（2/2）")
    + example(
        """
<table class="extbl ex4">
<tr><th>困ったこと</th><th>誰に</th><th>いつ</th><th>どう伝える？</th></tr>
<tr><td>仕事量が多すぎる</td><td>上司</td><td>週1回の1on1</td><td>「今のタスクを一覧にしました。優先順位を一緒に決めてもらえますか」</td></tr>
<tr><td>眠れない日が続く</td><td>家族→医師</td><td>1週間続いたら</td><td>「最近眠れなくて、少し話を聞いてほしい」</td></tr>
</table>"""
    )
    + '<div class="hs-title">伝え方のヒント</div>'
    + '<div class="tips"><p>① 事実（何が起きているか）　② 影響（どう困っているか）　③ お願い（どうしてほしいか）<br>の順で話すと、感情的にならずに伝えやすくなります。</p></div>'
    + summary(
        '<div class="hs-title">私の相談ルート</div>'
        + """<table class="tbl route-sum">
<tr><th>こんなとき</th><th>まず相談する人</th><th>次に相談する人</th></tr>
<tr><td>仕事のこと</td><td></td><td></td></tr>
<tr><td>人間関係のこと</td><td></td><td></td></tr>
<tr><td>心や体のこと</td><td></td><td></td></tr>
<tr><td>これからのキャリアのこと</td><td></td><td></td></tr>
</table>"""
    )
    + reflect("困ったときの相談先", "<p>「私の相談ルート」を、最終版の取扱説明書に書き写しましょう。</p>"),
    step=2,
)

# =====================================================================
# STEP3
# =====================================================================
step_door(
    3,
    "推奨：3か月目",
    "残る・辞める・転職するをどう判断するか？",
    "STEP1・2で整理した内容をもとに、これからの働き方を選びます。<br>"
    "その場の感情だけで決めるのではなく、<b>自分の基準</b>で比べること。<br>そして、分かったことを具体的な行動に変えていきます。",
    [("ワーク8", "残る・環境を変える判断基準"), ("ワーク9", "Must・Want・NG"), ("ワーク10", "90日行動計画")],
)

# ---------------- ワーク8 ----------------
W8_ITEMS = ["消耗ポイント", "働きやすい条件", "仕事量", "人間関係", "給与", "将来性", "心身への負担", "改善可能性", "やりたい仕事", "家庭との両立"]
w8rows = "".join(f"<tr><th>{t}</th><td></td><td></td><td></td><td></td></tr>" for t in W8_ITEMS)
page(
    work_head(3, 8, "残る・環境を変える判断基準", "感情だけでなく、自分の基準で働き方を選ぶ。", "（1/3）")
    + explain(
        "<p>しんどいときは「今すぐ辞めたい」か「我慢するしかない」に偏りがちです。<br>"
        "4つの選択肢を<b>同じ項目で並べて比べる</b>と、冷静に判断しやすくなります。</p>"
        "<p>それぞれのマスに <b>○（良い）△（どちらとも）×（よくない）</b> を書き入れ、気づいたことを一言メモしましょう。</p>"
    )
    + f"""
<table class="tbl cmp-tbl">
<tr><th>判断項目</th><th>今の会社に<br>残る</th><th>今の会社で<br>働き方を調整する</th><th>異動する</th><th>転職を<br>検討する</th></tr>
{w8rows}
<tr><th>その他<br>（　　　　）</th><td></td><td></td><td></td><td></td></tr>
</table>
<p class="small">※「消耗ポイント」はワーク2、「働きやすい条件」はワーク3の内容を見ながら考えると、判断しやすくなります。</p>""",
    step=3,
)
OPTS = ["今の会社に残る", "今の会社で働き方を調整する", "異動する", "転職を検討する"]
page(
    work_head(3, 8, "残る・環境を変える判断基準", None, "（2/3）")
    + '<p class="qnote">比較表を見ながら、それぞれの選択肢の「よい点」と「気になる点」を書き出しましょう。</p>'
    + '<div class="grid2">'
    + "".join(
        f'<div class="card opt"><div class="card-h">{o}</div><div class="ol">よい点</div>{lines(4, 8)}<div class="ol">気になる点</div>{lines(4, 8)}</div>'
        for o in OPTS
    )
    + "</div>"
    + example(
        "<p><b>今の会社で働き方を調整する</b><br>よい点：給与や通勤は今のまま。電話当番の調整は上司も前向きだった。<br>"
        "気になる点：繁忙期の突発対応は変わらなそう。半年後も同じ状態なら厳しい。</p>"
    ),
    step=3,
)
page(
    work_head(3, 8, "残る・環境を変える判断基準", None, "（3/3）")
    + summary(
        '<div class="hs-title">現時点での私の判断</div>'
        + checks(OPTS + ["まだ決めない（期限：　　月　　日まで様子を見る）"], 2)
        + '<div class="hs-title">その理由</div>'
        + lines(5)
    )
    + reflect(
        "今の会社に残れる条件／環境を変える・転職を検討するサイン",
        '<div class="grid2 tight">'
        + f'<div><p><b>今の会社に残れる条件</b><br><span class="small">これが満たされていれば続けられる</span></p>{lines(6, 8)}</div>'
        + f'<div><p><b>環境を変える・転職を検討するサイン</b><br><span class="small">これが起きたら本格的に動く</span></p>{lines(6, 8)}</div>'
        + "</div>",
    )
    + example(
        "<p><b>残れる条件：</b>月の残業が20時間以内／電話当番が週2日以内<br>"
        "<b>検討するサイン：</b>3か月相談しても仕事量が変わらない／休日も疲れが抜けない状態が1か月続く</p>"
    )
    + '<p class="small">※判断は「今の時点での仮の答え」で大丈夫です。状況が変われば、何度でも見直せます。</p>',
    step=3,
)

# ---------------- ワーク9 ----------------
page(
    work_head(3, 9, "Must・Want・NG", "次の職場を選ぶとき、「やりたいこと」だけでなく「絶対にやりたくないこと」を明確にする。", "（1/4）")
    + '<div class="mwn">'
    + '<div class="mw m"><div class="mwh">Must</div><b>絶対に必要な条件</b><p>これがないと長く働けない</p></div>'
    + '<div class="mw w"><div class="mwh">Want</div><b>できれば欲しい条件</b><p>あるとうれしい・優先度は中</p></div>'
    + '<div class="mw n"><div class="mwh">NG</div><b>絶対に避けたい条件</b><p>これがあるなら選ばない</p></div>'
    + "</div>"
    + explain(
        "<p>転職を考えるとき、多くの人は「何をやりたいか」「どんな条件がいいか」から考えます。<br>"
        "でも、やりたいことは迷いやすく、求人の魅力的な言葉にも揺れやすいもの。</p>"
        "<p>一方で、<b>「これだけは避けたい」</b>は、これまでの消耗した経験から具体的に書くことができます。<br>"
        "HSP気質の人にとっては、<b>NGを先に決めておくこと</b>が、同じ消耗を繰り返さないための大きな助けになります。</p>",
        "なぜ「NG」が大切なのか",
    )
    + """
<div class="voice">
  <div class="vh">運営者の体験から</div>
  <p>私自身も転職する前に、<b>「絶対にやりたくないことリスト」</b>をつくり、それをもとに転職先を選びました。</p>
  <p>「やりたいこと」だけで探していると、どの求人も良さそうに見えて迷ってしまいます。<br>
  でも、「これは絶対に避けたい」が決まっていると、<b>選ばない理由がはっきりする</b>ので、判断がぐっとラクになります。</p>
  <p>このワークでは、その考え方をそのまま使います。</p>
</div>
<div class="hs-title">ヒント：NGはこれまでのワークから見つかります</div>
<div class="tips"><p>・ワーク2「私が消耗しやすい条件 TOP5」「避けたい・注意したい条件」<br>
・ワーク4「私が頑張りすぎ始める3つのパターン」（その状況を生みやすい職場は？）<br>
・ワーク5「自分では変えにくいこと」（次の職場でも同じだったら？）</p></div>
""",
    step=3,
)
W9_ITEMS = ["残業時間", "通勤時間", "年収", "リモートワーク", "電話対応", "出張", "転勤", "人間関係", "職場の静かさ", "マルチタスク", "個人作業／チーム作業", "裁量", "評価制度", "管理職", "休日", "業務内容"]
w9rows = "".join(f'<tr><th>{t}</th><td class="c"><i class="ci"></i></td><td class="c"><i class="ci"></i></td><td class="c"><i class="ci"></i></td><td></td></tr>' for t in W9_ITEMS)
page(
    work_head(3, 9, "Must・Want・NG", None, "（2/4）")
    + '<p class="qnote">各項目について、Must・Want・NGのどれに当たるかを○で囲み、具体的な条件をメモしましょう。<br>どれにも当てはまらない項目は空欄で構いません。</p>'
    + f"""
<table class="tbl mwn-tbl">
<tr><th>検討項目</th><th>Must</th><th>Want</th><th>NG</th><th>具体的な条件メモ</th></tr>
{w9rows}
</table>
<p class="small">例：残業時間 ── Must「月20時間以内」／電話対応 ── NG「一日中電話を受ける業務」</p>""",
    step=3,
)
page(
    work_head(3, 9, "Must・Want・NG", None, "（3/4）")
    + '<p class="qnote">前のページをもとに、Must・Want・NGを整理しましょう。数が多いときは、大事な順に並べ替えてみてください。</p>'
    + '<div class="mwn-cols">'
    + f'<div class="mc m"><div class="mch">Must｜絶対に必要</div>{numbered(5, h=17)}</div>'
    + f'<div class="mc w"><div class="mch">Want｜できれば欲しい</div>{numbered(5, h=17)}</div>'
    + f'<div class="mc n"><div class="mch">NG｜絶対に避けたい</div>{numbered(5, h=17)}</div>'
    + "</div>"
    + example(
        '<div class="ex3"><div><b>Must</b><p>月の残業20時間以内／一人で集中できる時間がある／年収は現状維持以上</p></div>'
        "<div><b>Want</b><p>週2日以上のリモート／通勤45分以内／評価基準が明文化されている</p></div>"
        "<div><b>NG</b><p>電話対応がメイン業務／常に複数案件を同時進行／全国転勤あり</p></div></div>"
    )
    + summary("<p>Mustは<b>3〜5個</b>に絞るのがおすすめです。Mustが多すぎると、当てはまる職場が見つかりにくくなります。<br>迷うものはWantに入れておきましょう。</p>"),
    step=3,
)
page(
    '<div class="emph-page">'
    + work_head(3, 9, "Must・Want・NG", None, "（4/4）")
    + """
<div class="nglist">
  <div class="ng-h"><span class="ng-badge">重要</span><h3>絶対にやりたくないことリスト</h3></div>
  <p class="ng-lead">次の職場を選ぶときに、<b>「これがあるなら選ばない」</b>と言えることを5〜10個書き出しましょう。<br>
  仕事内容・働き方・環境・人間関係など、どんな角度からでも構いません。</p>"""
    + numbered(10, h=13.5, cls="ngnum")
    + "</div>"
    + example("<p>・一日の大半が電話対応の仕事　・毎日のように急な予定変更がある部署　・成果より「長く残ること」が評価される職場</p>")
    + reflect(
        "次の職場のMust条件／次の職場のNG条件／絶対にやりたくないこと",
        "<p>このリストは、最終版の取扱説明書に書き写し、<b>求人を見るとき・面接で質問するとき</b>のチェックリストとして使いましょう。</p>",
    )
    + "</div>",
    step=3,
)

# ---------------- ワーク10 ----------------
def w10_block(name, desc, cls):
    rows = "".join('<tr><td></td><td></td><td></td><td class="c"><i class="box"></i></td></tr>' for _ in range(2))
    return f"""
<div class="act {cls}"><div class="act-h"><b>{name}</b><span>{desc}</span></div>
<table class="tbl act-tbl"><tr><th>行動</th><th>期限</th><th>最初の一歩</th><th>完了</th></tr>{rows}</table></div>"""


page(
    work_head(3, 10, "90日行動計画", "分かっただけで終わらず、行動につなげる。", "（1/2）")
    + explain(
        "<p>大きな決断より、<b>小さな一歩</b>を積み重ねることが大切です。<br>"
        "「最初の一歩」は、<b>5分でできるくらい小さく</b>するのがコツです。</p>"
    )
    + w10_block("やめること", "消耗の原因になっている習慣・引き受け方", "a1")
    + w10_block("始めること", "自分を守る・整えるための新しい行動", "a2")
    + w10_block("相談すること", "上司・家族・専門家などに話すこと", "a3")
    + w10_block("調べること", "異動制度・求人・相談窓口など、情報を集めること", "a4"),
    step=3,
)
page(
    work_head(3, 10, "90日行動計画", None, "（2/2）")
    + example(
        """
<table class="extbl ex4">
<tr><th>分類</th><th>行動</th><th>期限</th><th>最初の一歩</th></tr>
<tr><td>やめること</td><td>依頼に即答する</td><td>今月から</td><td>「確認して返事します」を付箋に書いてPCに貼る</td></tr>
<tr><td>相談すること</td><td>電話当番の見直し</td><td>11/15</td><td>次の1on1の議題に入れる</td></tr>
<tr><td>調べること</td><td>社内公募制度</td><td>11/30</td><td>社内ポータルで「異動」と検索する</td></tr>
</table>"""
    )
    + '<div class="hs-title">ふりかえりチェックポイント</div>'
    + '<div class="cp3">'
    + f'<div class="cp"><div class="cph">30日後｜　　月　　日</div><p class="small">できたこと・続かなかったこと</p>{lines(8, 8)}</div>'
    + f'<div class="cp"><div class="cph">60日後｜　　月　　日</div><p class="small">変化したこと・調整したいこと</p>{lines(8, 8)}</div>'
    + f'<div class="cp"><div class="cph">90日後｜　　月　　日</div><p class="small">次の90日で続けること</p>{lines(8, 8)}</div>'
    + "</div>"
    + summary("<p>できなかった行動があっても大丈夫です。「なぜ難しかったか」も、自分を知る大切な材料になります。</p>")
    + reflect("これから90日でやること", "<p>4つの分類から、<b>特に大事な行動を3つ</b>選んで、最終版の取扱説明書に書き写しましょう。</p>"),
    step=3,
)

# =====================================================================
# 最終版
# =====================================================================
page(
    """
<div class="door">
  <div class="door-month">仕上げ</div>
  <div class="door-lab">最終版</div>
  <h2 class="door-name">私の働き方の<br>取扱説明書</h2>
  <div class="door-theme"><span>ゴール</span>自分の働き方を、自分の言葉で説明できる</div>
  <p class="door-desc">各ワークの「取扱説明書に反映する内容」を、次の2ページに書き写していきます。<br>
  完成したら、ここに書かれた言葉が、迷ったときの<b>あなた自身の判断基準</b>になります。</p>
  <ul class="door-works">
    <li><span>ワーク2</span>消耗しやすい条件</li><li><span>ワーク3</span>働きやすい条件</li>
    <li><span>ワーク4</span>頑張りすぎるパターン</li><li><span>ワーク6</span>働き方ルール</li>
    <li><span>ワーク7</span>相談先</li><li><span>ワーク5・8</span>残れる条件・検討サイン</li>
    <li><span>ワーク9</span>Must・NG・やりたくないこと</li><li><span>ワーク10</span>90日でやること</li>
  </ul>
</div>""",
    step="F",
    cls="p-door",
)


def hsec(title, src, body, cls=""):
    return f'<div class="hsec {cls}"><div class="hsh"><b>{title}</b><span>{src}</span></div>{body}</div>'


page(
    """<div class="hb-top"><div class="hb-title"><span>HSPの働き方ゼミ</span><h2>私の働き方の取扱説明書</h2></div>
<div class="hb-meta"><div>名前<i></i></div><div>最終更新日<i>　　年　　月　　日</i></div></div></div>"""
    + '<div class="grid2 tight">'
    + hsec("私が消耗しやすい条件 TOP5", "ワーク2", numbered(5, h=10))
    + hsec("私が働きやすい条件 TOP5", "ワーク3", numbered(5, h=10))
    + "</div>"
    + hsec("私が頑張りすぎる3つのパターン", "ワーク4", numbered(3, h=10.5))
    + hsec("私を守る5つの働き方ルール", "ワーク6", numbered(5, h=10))
    + hsec(
        "困ったときの相談先",
        "ワーク7",
        '<table class="tbl hb-route"><tr><th>こんなとき</th><th>まず相談する人</th><th>次に相談する人</th></tr>'
        "<tr><td>仕事のこと</td><td></td><td></td></tr><tr><td>人間関係のこと</td><td></td><td></td></tr>"
        "<tr><td>心や体のこと</td><td></td><td></td></tr><tr><td>キャリアのこと</td><td></td><td></td></tr></table>",
    ),
    step="F",
    cls="p-hb",
)
page(
    '<div class="hb-top small-top"><div class="hb-title"><span>HSPの働き方ゼミ</span><h2>私の働き方の取扱説明書（2/2）</h2></div></div>'
    + '<div class="grid2 tight">'
    + hsec("今の会社に残れる条件", "ワーク5・8", numbered(3, h=10))
    + hsec("環境を変える・転職を検討するサイン", "ワーク8", numbered(3, h=10))
    + hsec("次の職場のMust条件", "ワーク9", numbered(4, h=10))
    + hsec("次の職場のNG条件", "ワーク9", numbered(4, h=10))
    + "</div>"
    + hsec("絶対にやりたくないこと", "ワーク9", '<div class="grid2 tight">' + numbered(5, h=9.6) + numbered(5, start=6, h=9.6) + "</div>", "hs-ng")
    + hsec(
        "これから90日でやること",
        "ワーク10",
        '<table class="tbl hb-act"><tr><th>行動</th><th>期限</th><th>完了</th></tr>'
        + "".join('<tr><td></td><td></td><td class="c"><i class="box"></i></td></tr>' for _ in range(3))
        + "</table>",
    )
    + '<div class="hb-foot"><div>最終更新日<i>　　年　　月　　日</i></div><div>次回見直し予定日<i>　　年　　月　　日</i></div></div>',
    step="F",
    cls="p-hb",
)
page(
    """
<div class="msg">
  <div class="msg-mark"></div>
  <h2>この取扱説明書は、<br>「正解」ではなく「仮説」です。</h2>
  <p>この「働き方の取扱説明書」は、一度完成したら終わりではありません。</p>
  <p>上司、部署、仕事内容、家庭環境、年齢などが変われば、<br>自分に合う働き方も変わっていきます。</p>
  <p>ここに書いたことは、<b>今の自分にとっての「仮説」</b>です。<br>うまくいかないことがあっても、それは失敗ではなく、<br>仮説を更新するための大切な材料です。</p>
  <p>半年後、1年後にまた見直し、<br>自分に合った働き方へ、少しずつ更新していきましょう。</p>
  <div class="msg-end">ここまで取り組んだ、あなた自身をねぎらってください。<br>本当にお疲れさまでした。</div>
</div>""",
    step="F",
    cls="p-msg",
)


# =====================================================================
# 見直し・更新ページ
# =====================================================================
def review_page(n):
    page(
        f'<div class="sec-label">REVIEW &amp; UPDATE</div><h2 class="sec-title">見直し・更新ページ<span class="part">（{n}回目）</span></h2>'
        '<p class="sec-lead">半年後・1年後など、働く環境や気持ちが変わったときに取扱説明書を見直しましょう。<br>見直した内容は、最終版のページやスプレッドシート版にも反映してください。</p>'
        '<div class="rv-dates"><div>前回更新日<i>　　年　　月　　日</i></div><div>今回の見直し日<i>　　年　　月　　日</i></div></div>'
        + field("今回見直した理由", 3)
        + '<div class="grid2 tight">'
        + field("変わったこと", 5)
        + field("変わらなかったこと", 5)
        + field("新しく追加した条件", 5)
        + field("手放した条件", 5)
        + "</div>"
        + field("見直してみて気づいたこと・次の自分へのメモ", 3)
        + '<div class="rv-dates"><div>次回見直し予定日<i>　　年　　月　　日</i></div></div>',
    )


review_page(1)
review_page(2)

# =====================================================================
# 注意事項
# =====================================================================
page(
    """
<div class="sec-label">NOTES</div>
<h2 class="sec-title">注意事項</h2>
<div class="caution">
  <div class="ch">ご利用にあたって</div>
  <p>このワークブックは、<b>HSPの診断、医療診断、心理療法、メンタル不調の治療を目的としたものではありません。</b></p>
  <p>強い心身の不調や、仕事・日常生活に大きな支障がある場合は、無理をせず<b>医療・心理等の専門家へご相談ください。</b></p>
</div>
<div class="note-list">
  <p>・ワークに取り組む中で、つらい記憶を思い出して気分が落ち込むことがあります。そのときは無理に続けず、いったん手を止めて休んでください。</p>
  <p>・転職・退職・異動などの最終的な判断は、ご自身の状況をふまえて、ご自身の責任で行ってください。</p>
  <p>・記入例は一例です。あなたの答えと違っていても、まったく問題ありません。</p>
  <p>・本ワークブックは「HSPの働き方ゼミ」メンバーの個人利用を目的としています。無断での転載・再配布はご遠慮ください。</p>
</div>
<div class="colophon">
  <div class="cb">HSPの働き方ゼミ</div>
  <div>働き方の取扱説明書　ワークブック版</div>
  <div>Version 1.0</div>
  <div class="small">併用教材：HSPの働き方ゼミ｜働き方の取扱説明書_v1.0（スプレッドシート版）</div>
</div>
""",
)

# =====================================================================
# 出力
# =====================================================================
CSS = open(os.path.join(HERE, "style.css"), encoding="utf-8").read().replace("__FONTDIR__", "file://" + os.path.join(HERE, "fonts"))

out = []
for i, (body, step, cls, footer) in enumerate(pages, 1):
    sc = STEPS[step][2] if step else "s0"
    tab = ""
    if step and "p-door" not in cls:
        lab, name, _ = STEPS[step]
        tab = f'<div class="steptab">{lab}｜{name}</div>'
    foot = f'<div class="pfoot"><span>{TITLE}　ワークブック v1.0</span><span class="pno">{i}</span></div>' if footer else ""
    out.append(f'<section class="page {sc} {cls}">{tab}<div class="pin">{body}</div>{foot}</section>')

html = f"""<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>{TITLE}_ワークブック_v1.0</title>
<style>{CSS}</style></head><body>{''.join(out)}</body></html>"""
with open(os.path.join(HERE, "workbook.html"), "w", encoding="utf-8") as f:
    f.write(html)
print("pages:", len(pages))
