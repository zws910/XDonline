import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner


# 配置xadmin全站的主题
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView, BaseSetting)


# 全局修改
class GlobalSettings(object):
    # 修改title
    site_title = '新道后台管理'
    # 修改footer
    site_footer = '新道文化教育公司'
    # 收起菜单
    menu_style = 'accordion'


# 将footer和title信息注册
xadmin.site.register(views.CommAdminView, GlobalSettings)


# 注册models
class EmailVerifyRecordAdmin(object):
    # 显示的列
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 搜索的字段, 不要添加时间搜索
    search_fields = ['code', 'email', 'send_type']
    # 过滤
    list_filter = ['code', 'email', 'send_type', 'send_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(Banner, BannerAdmin)
