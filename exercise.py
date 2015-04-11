#!/usr/bin/env python
# vim: fileencoding=utf-8

# rospy のインポート
import rospy
# 数学ライブラリ
import math
# 今回主に使うROSメッセージ型をインポート
from geometry_msgs.msg import Quaternion, PoseStamped
# 幾何学変換のための関数
from tf.transformations import quaternion_from_euler

# ノードの初期化
rospy.init_node('exercise')

# ゴール配信者オブジェクトを生成
goal_pub = rospy.Publisher('/move_base_simple/goal', # トピック名
                           PoseStamped,              # 型
                           queue_size=1,             # 送信キューのサイズ
                           latch=True)               # データを次の更新まで保持する

# 次のゴールのメッセージを生成して初期化
goal = PoseStamped()
goal.header.frame_id = 'world'        # 世界座標系で指定する
goal.header.stamp = rospy.Time.now()  # タイムスタンプは今の時間
goal.pose.position.x = 3.5
goal.pose.position.y = 3.5
goal.pose.position.z = 0.0
q = quaternion_from_euler(0, 0, math.radians(90))
goal.pose.orientation = Quaternion(*q)

goal_pub.publish(goal)  # 実際にメッセージを配信

# Ctrl−Cで中断するまでポーリング
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    rate.sleep()
