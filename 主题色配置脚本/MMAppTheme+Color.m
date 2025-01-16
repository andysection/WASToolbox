#import "MMAppTheme+Color.h"

@implementation MMAppTheme

#pragma mark + 颜色配置

///品牌色
+ (UIColor *)brandColor {
 	return HexColor(0x5935DE);
}
///辅助色一
+ (UIColor *)subColor1 {
 	return HexColor(0xC9BEFF);
}
///辅助色二
+ (UIColor *)subColor2 {
 	return HexColor(0xE9E5FF);
}
///警示色
+ (UIColor *)alertColor {
 	return HexColor(0xDD4D38);
}
///背景色深色
+ (UIColor *)darkBackgroundColor {
 	return HexColor(0x000000);
}
///背景色浅色
+ (UIColor *)lightBackgroundColor {
 	return HexColor(0xFFFFFF);
}
///选中色
+ (UIColor *)selectColor {
 	return HexColor(0x47944A);
}
///下划线分割线颜色
+ (UIColor *)lineColor {
 	return HexColor(0xA4A4A4);
}
///对话框颜色
+ (UIColor *)contentColor {
 	return HexColor(0xF2F2F2);
}
///一级字体颜色
+ (UIColor *)mainTextColor {
 	return HexColor(0x000000);
}
///二级字体颜色
+ (UIColor *)subTextColor {
 	return HexColor(0x666666);
}
///辅助字体颜色
+ (UIColor *)otherTextColor {
 	return HexColor(0x797979);
}
///辅助字体颜色深色背景时
+ (UIColor *)mainTextColorForDark {
 	return HexColor(0xFFFFFF);
}
///按钮背景色3
+ (UIColor *)BTNBgColor5935DE {
 	return HexColor(0x5935DE);
}
///按钮背景色2
+ (UIColor *)BTNBgColorC0C0C0 {
 	return HexColor(0xC0C0C0);
}
///按钮背景色1
+ (UIColor *)BTNBgColorFFFFFF {
 	return HexColor(0xFFFFFF);
}
///按钮文字色1
+ (UIColor *)BTNTextColor000000 {
 	return HexColor(0x000000);
}
///按钮文字色2
+ (UIColor *)BTNTextColorFFFFFF {
 	return HexColor(0xFFFFFF);
}
///按钮文字色3
+ (UIColor *)BTNTextColor797979 {
 	return HexColor(0x797979);
}
@end
