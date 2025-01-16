#import <Foundation/Foundation.h>

@interface MMAppTheme (Color)

#pragma mark - 字体配置

///品牌色 + 0x5935DE
+ (UIColor *)brandColor;

///辅助色一 + 0xC9BEFF
+ (UIColor *)subColor1;

///辅助色二 + 0xE9E5FF
+ (UIColor *)subColor2;

///警示色 + 0xDD4D38
+ (UIColor *)alertColor;

///背景色深色 + 0x000000
+ (UIColor *)darkBackgroundColor;

///背景色浅色 + 0xFFFFFF
+ (UIColor *)lightBackgroundColor;

///选中色 + 0x47944A
+ (UIColor *)selectColor;

///下划线分割线颜色 + 0xA4A4A4
+ (UIColor *)lineColor;

///对话框颜色 + 0xF2F2F2
+ (UIColor *)contentColor;

///一级字体颜色 + 0x000000
+ (UIColor *)mainTextColor;

///二级字体颜色 + 0x666666
+ (UIColor *)subTextColor;

///辅助字体颜色 + 0x797979
+ (UIColor *)otherTextColor;

///辅助字体颜色深色背景时 + 0xFFFFFF
+ (UIColor *)mainTextColorForDark;

///按钮背景色3 + 0x5935DE
+ (UIColor *)BTNBgColor5935DE;

///按钮背景色2 + 0xC0C0C0
+ (UIColor *)BTNBgColorC0C0C0;

///按钮背景色1 + 0xFFFFFF
+ (UIColor *)BTNBgColorFFFFFF;

///按钮文字色1 + 0x000000
+ (UIColor *)BTNTextColor000000;

///按钮文字色2 + 0xFFFFFF
+ (UIColor *)BTNTextColorFFFFFF;

///按钮文字色3 + 0x797979
+ (UIColor *)BTNTextColor797979;

@end
