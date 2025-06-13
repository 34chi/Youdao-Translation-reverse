
import CryptoJS from 'crypto-js'

const md5 = str => CryptoJS.MD5(str).toString().toUpperCase()

const a = (new Date).getTime();

const g='asdjnjfenknafdfsdfsd'

const d='fanyideskweb'

const u="webfanyi"
const sign = S(a, g)


function S(e, t) {
    return `client=${d}&mysticTime=${e}&product=${u}&key=${t}`
}

md5(sign)


console.log(md5(sign))
