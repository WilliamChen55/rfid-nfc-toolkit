# SEO 关键词与首批选题（15 个）

> 所有内容最终落地到独立站 hackerwarehouse.me；GitHub 仓库只做技术信任与引流入口。
>
> 原则：**搜"协议/设备/开发"，不搜"攻破/复制"**。前者能长期排名，后者既排不上也招风控。

## 一、15 个关键词（按意图分组）

### 意图 A：开发者找工具（转化最高）
| # | 关键词 | 建议页面 |
| --- | --- | --- |
| 1 | `rfid reader python library` | 首页 / docs |
| 2 | `ISO14443A python` | docs/protocols |
| 3 | `read ATQA SAK from tag` | 博客长文 |
| 4 | `ISO15693 python inventory` | 博客长文 |
| 5 | `pyserial rfid reader` | docs/getting-started |

### 意图 B：硬件型号（自带流量）
| # | 关键词 | 建议页面 |
| --- | --- | --- |
| 6 | `proxmark3 python wrapper` | 产品页/博客 |
| 7 | `ACR122U python example` | 教程 |
| 8 | `PN532 UART python` | 教程 |
| 9 | `flipper zero serial bridge python` | 教程 |
| 10 | `chameleon ultra python api` | 教程 |

### 意图 C：场景与合规（企业客户）
| # | 关键词 | 建议页面 |
| --- | --- | --- |
| 11 | `rfid asset tagging inventory software` | 行业页 |
| 12 | `access control system testing tools` | 行业页（合规口径） |
| 13 | `rfid tag compatibility checker` | 工具页 |
| 14 | `nfc protocol analyzer tool` | 工具页 |
| 15 | `rfid reader sensitivity comparison` | 测评长文 |

## 二、首批 15 篇选题（3 个月排期，每周 1–2 篇）

1. What ATQA and SAK actually tell you about a tag
2. ISO14443-A vs ISO14443-B: frame formats side by side
3. Reading ISO15693 asset tags in Python
4. CRC-A and CRC-B: the two checksums you keep getting wrong
5. ACR122U + Python: PC/SC from zero
6. PN532 UART mode: wiring, baud, and first frame
7. Proxmark3 client bridge: turning CLI output into JSON
8. Flipper Zero as a serial bridge for scripted tests
9. Building a tag compatibility checker for your own lab
10. Reader sensitivity comparison: how to measure read range honestly
11. Tag families explained: Ultralight, Classic, Plus, DESFire, CPU cards
12. Designing an asset-tagging pipeline that survives audits
13. What "authorized testing" means in practice for access systems
14. 13.56 MHz antenna detuning: why your tag stops responding
15. From CLI to CI: testing a reader fleet automatically

## 三、写作规范（避免风控与降权）

- 标题里不出现 clone / crack / bypass / duplicate / universal
- 每篇结尾统一一段 Legal Notice，链到 `LEGAL_NOTICE.md`
- 每篇配 1 张自己的实测图（CLI 输出或示波器/频谱截图），提升原创度
- 内部互链：老文链新文，形成主题簇（topic cluster）
- 站点地图 + Bing/Google Search Console 提交，别只等自然收录

## 四、GitHub 侧配合

每个关键词对应一个仓库里可被索引的位置：README 章节、docs 页面标题、issue 模板字段、release notes 摘要。GitHub 搜索和 Google 都会索引这些文本。
